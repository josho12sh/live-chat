import socket
import threading
import sys

client = socket.socket()

try:
    client.connect(("localhost", 8000))
except ConnectionRefusedError:
    print("Server is down. Please try again later.")
    sys.exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024)
            if not message:
                print("\nServer closed connection.")
                break
            print(f"\nAnother user said: {message.decode()}")
        except (ConnectionResetError, OSError):
            print("\nServer shut down.")
            break
            
    # Force close the socket to break the main thread's input/send loop
    client.close() 

client_thread = threading.Thread(target=receive_messages)
# 1. Make the thread a daemon so it dies when the main thread dies
client_thread.daemon = True 
client_thread.start()

while True:
    try:
        message = input("You: ")
    except OSError:
        # This triggers if the background thread closes the socket while input() is waiting
        break

    if message == "/quit":
        break

    try:
        client.sendall(message.encode())
    except (ConnectionResetError, OSError):
        print("Server shut down.")
        break

    print("Message sent!")
    
client.close()
