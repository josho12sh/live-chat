import socket
import threading

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.sendall(message)
    
def handle_client(connection, address):
    print(f"{address[0]} connected to the server.")

    while True:

        try:
            message = connection.recv(1024)

        except ConnectionResetError:
            print("Client forcibly disconnected.")
            break

        if not message:
            print("Client disconnected.")
            break

        broadcast(message, connection)

    clients.remove(connection)
    connection.close()

server = socket.socket()

server.bind(("localhost", 8000))

server.listen()

print("Waiting for connection...")

while True:
    connection, address = server.accept()
    clients.append(connection)

    client_thread = threading.Thread(
        target=handle_client,
        args=(connection, address)
    )

    client_thread.start()
    