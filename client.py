import socket
import threading

client = socket.socket()
client.connect(("localhost", 8000))

def receive_messages():
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print(f"\nAnother user said: {message.decode()}")
        except ConnectionResetError:
            print("\nServer shut down.")
            break

client_thread = threading.Thread(
    target=receive_messages
)

client_thread.start()

while True:
    message = input("You: ")

    if message == "/quit":
        break

    client.sendall(message.encode())
    print("Message sent!")
    
client.close()