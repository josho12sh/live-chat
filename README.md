# Live Chat Server

A from-scratch Python networking project that started as a simple TCP
client/server chat system.

The long-term goal is to develop this into a web-based live chat
application using FastAPI, HTML, CSS, JavaScript, and WebSockets.

## Current Version

**v0.3.1 — Multi-Client TCP Prototype**

## Features

- TCP client/server communication
- Client connects to a local server
- Client can send messages to the server
- Server receives and broadcasts messages to connected clients
- Multiple clients can connect simultaneously
- Threaded client handling
- Client can receive messages while waiting for or sending messages
- `/quit` command for the client
- Basic client disconnect handling
- Server handles forced disconnections from clients
- Error handling for cases in which server is down for clients

## Project Structure

```text
Live Chat Server/

├── client.py
├── server.py
├── requirements.txt
├── VERSION
├── README.md
└── .gitignore