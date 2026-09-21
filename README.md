# Live Chat Server

A from-scratch Python networking project that started as a simple TCP
client/server chat system.

The long-term goal is to develop this into a web-based live chat
application using FastAPI, HTML, CSS, JavaScript, and WebSockets.

## Current Version

**v0.2.0 — Initial TCP Prototype**

## Features

- TCP client/server communication
- Client connects to a local server
- Client can send messages to the server
- Server receives and displays messages
- `/quit` command for the client
- Server handles forced disconnected from the client
- Basic client disconnect handling

## Project Structure

```text
Live Chat Server/
│
├── client.py
├── server.py
├── requirements.txt
├── VERSION
├── README.md
└── .gitignore