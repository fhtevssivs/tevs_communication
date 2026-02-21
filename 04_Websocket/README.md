# How to Start the WebSocket Chat Server Demo

This project demonstrates a basic web-based chat server using **WebSockets** powered by Flask and Flask-SocketIO.

---

## Step 1 (Option A): Start Chat Server in Docker

> Use this option if you want to run the chat server inside a Docker container.

Make sure Docker and Docker Compose are installed.

Start the chat server with:

```bash
docker-compose -f docker-compose.yml up -d
```

---

## Step 1 (Option B): Start Chat Server with Python

> Use this option if you prefer to run the server locally with Python.

Install the required dependencies (if not already installed):

```bash
pip install -r server/requirements.txt
```

Then start the server:

```bash
python server/main.py
```

---

## Step 2: Open the Chat Interface

Open your web browser and go to:
http://localhost:4001

You can now test the chat functionality by opening the page in multiple tabs or windows.

---

## Notes

- The chat server uses Flask-SocketIO for real-time communication.
- Messages are broadcast to all connected clients.
- The frontend is located in `templates/chat.html` and styled using Bootstrap.

