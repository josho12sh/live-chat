import socket

server = socket.socket()

server.bind(("localhost", 8000))

server.listen()

print("Waiting for connection...")

while True:
    connection, address = server.accept()

    print(f"{address[0]} connected to the server.")

    while True:

        message = connection.recv(1024)

        if not message:
            print("Client disconnected.")
            break

        print(f"Client said: {message.decode()}")

    connection.close()