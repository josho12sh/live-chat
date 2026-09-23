# Live Chat Server

A from-scratch Python networking project that started as a simple TCP client/server chat system.

The long-term goal is to develop this into a web-based live chat application using FastAPI, HTML, CSS, JavaScript, and WebSockets.

## Current Version

**v1.0.0 — First Functional Release**

## Features

* TCP client/server communication
* Client connects to a local server
* Client can send messages
* Server receives and broadcasts messages to connected clients
* Multiple simultaneous clients
* Threaded client handling
* Client can receive messages while waiting/sending
* `/quit`
* Basic client disconnect handling
* Server handles forced client disconnections
* Client error handling if the server is down
* Real-time terminal input using `msvcrt`
* Immediate `[You]` prompt
* Cleaner terminal formatting
* Incoming messages displayed without permanently destroying the current input line
* Current input restored after incoming messages
* Type hints throughout the client and server
* Code comments and documentation

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/josho12sh/live-chat.git
cd live-chat
```

### 2. Start the server

Run:

```bash
python server.py
```

You should see:

```text
Waiting for connection...
```

### 3. Start a client

Open another terminal in the project directory and run:

```bash
python client.py
```

The client will connect to the server and allow you to send messages.

### 4. Connect multiple clients

You can run `client.py` multiple times to connect multiple clients to the same server.

Messages sent by one client will be broadcast to the other connected clients.

### Connecting From Another Computer

The default configuration uses:

```text
localhost:8000
```

`localhost` refers to the computer running the program itself.

To allow clients on another computer on the same network to connect, the server and client addresses need to be configured for the server computer's local network IP address, and the server must listen on an address that accepts network connections.

You will also need to make sure port `8000` is allowed through the server computer's firewall.

## Project Structure

```text
live-chat/
│
├── client.py
├── server.py
├── requirements.txt
├── VERSION
├── README.md
└── .gitignore
```

## Version History

### v1.0.0 — First Functional Release

* Completed the core TCP chat functionality
* Added multi-client support
* Added message broadcasting
* Added threaded client handling
* Added real-time terminal input
* Added client and server disconnect handling
* Added server-down error handling
* Added `/quit`
* Added type hints
* Improved code comments and documentation

This is the first release where the project provides its intended core functionality: clients can connect to a server and communicate with each other in real time.
