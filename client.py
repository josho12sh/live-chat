import socket

client = socket.socket()
client.connect(("localhost", 8000))

while True:
    message = input("Enter your message to the server: ")

    if message == "/quit":
        break

    client.sendall(message.encode())

    print("Message sent!")

client.close()