import socket
import threading

def handle_client(connection, server):
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

        print(f"Client said: {message.decode()}")

    connection.close()

server = socket.socket()

server.bind(("localhost", 8000))

server.listen()

print("Waiting for connection...")

while True:
    connection, address = server.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(connection, address)
    )

    client_thread.start()
    