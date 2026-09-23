# Imported Modules
import socket
import threading
import msvcrt
import sys


# Connection and Creation of Socket
client: socket.socket = socket.socket()

try:
    client.connect(("localhost", 8000))
except ConnectionRefusedError:
    print("Server is down. Please try again later.")
    sys.exit()


# Create message and lock for threading
message: str = ""
threading_lock: threading.Lock = threading.Lock()


def receive_messages() -> None:
    global message

    while True:
        try:
            received_message: bytes = client.recv(1024)

            if not received_message:
                print("\nServer closed connection.")
                break

            # Lock terminal output while displaying an incoming message.
            with threading_lock:

                sys.stdout.write("\r\033[K")
                sys.stdout.flush()

                print(f"[User] {received_message.decode()}")

                sys.stdout.write(f"[You] {message}")
                sys.stdout.flush()

        except (ConnectionResetError, OSError):
            print("\nServer shut down.")
            break

    # Force close the socket to break the main thread's input/send loop.
    client.close()


client_thread: threading.Thread = threading.Thread(target=receive_messages)

# Make the thread a daemon so it dies when the main thread dies.
client_thread.daemon = True
client_thread.start()


while True:
    try:
        sys.stdout.write("[You] ")
        sys.stdout.flush()

        while True:
            key: bytes = msvcrt.getch()
            deciphered_key: str = key.decode()

            if deciphered_key == "\r":
                sys.stdout.write("\n")
                break

            message += deciphered_key

            sys.stdout.write(deciphered_key)
            sys.stdout.flush()

    except OSError:
        # This triggers if the background thread closes the socket while input is waiting.
        break

    if message == "/quit":
        break

    try:
        client.sendall(message.encode())
        message: str = ""

    except (ConnectionResetError, OSError):
        print("Server shut down.")
        break


client.close()
