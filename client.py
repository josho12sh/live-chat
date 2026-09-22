import socket
import threading
import msvcrt
import sys

client = socket.socket()

try:
    client.connect(("localhost", 8000))
except ConnectionRefusedError:
    print("Server is down. Please try again later.")
    sys.exit()

message = ""
threading_lock = threading.Lock()

def receive_messages():
    global message

    while True:
        try:
            received_message = client.recv(1024)

            if not received_message:
                print("\nServer closed connection.")
                break

            with threading_lock:    

                sys.stdout.write("\r\033[K")
                sys.stdout.flush()

                print(f"[User] {received_message.decode()}")

                sys.stdout.write(f"[You] {message}")
                sys.stdout.flush()
                
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
        sys.stdout.write("[You] ")
        sys.stdout.flush()
        while True:
            key = msvcrt.getch()
            key = key.decode()

            if key == "\r":
                sys.stdout.write("\n")
                break

            message += key

            sys.stdout.write(key)
            sys.stdout.flush()


    except OSError:
        # This triggers if the background thread closes the socket while input() is waiting
        break

    if message == "/quit":
        break

    try:
        client.sendall(message.encode())
        message = ""
    except (ConnectionResetError, OSError):
        print("Server shut down.")
        break
    
client.close()
