# Imported Modules
import socket
import threading


# Store all currently connected client sockets.
clients: list[socket.socket] = []


def broadcast(message: bytes, sender: socket.socket) -> None:
    # Send the message to every connected client except the sender.
    for client in clients:
        if client != sender:
            client.sendall(message)


def handle_client(connection: socket.socket, address: tuple) -> None:
    print(f"{address[0]} connected to the server.")

    while True:
        try:
            message: bytes = connection.recv(1024)

        except ConnectionResetError:
            print("Client forcibly disconnected.")
            break

        if not message:
            print("Client disconnected.")
            break

        broadcast(message, connection)

    # Remove the disconnected client from the active client list.
    clients.remove(connection)
    connection.close()


# Create the server socket.
server: socket.socket = socket.socket()

server.bind(("localhost", 8000))

server.listen()

print("Waiting for connection...")


while True:
    connection: socket.socket
    address: tuple

    connection, address = server.accept()
    clients.append(connection)

    # Give each client its own thread so multiple clients can communicate simultaneously.
    client_thread: threading.Thread = threading.Thread(
        target=handle_client,
        args=(connection, address)
    )

    client_thread.start()