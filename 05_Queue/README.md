# How to Start the RabbitMQ Messaging Example

This project demonstrates a basic messaging flow using RabbitMQ, Docker, and Python.

## Step 1: Start RabbitMQ with Docker

Make sure Docker and Docker Compose are installed.

Start RabbitMQ:

```bash
docker-compose -f docker-compose.yml up -d
```

RabbitMQ Management UI is available at:  
http://localhost:15672

Default credentials:
- Username: `guest`
- Password: `guest`

## Step 2 (Optional): Install Python Dependencies

> Only needed if the required Python packages (e.g. `pika`) are not yet installed.

```bash
pip install -r client/requirements.txt
```

## Step 3: Run the Producer (Client)

This script sends a message to the queue every 5 seconds.

```bash
python client/main.py
```

## Step 4: Run the Consumer

This script receives messages from the queue and logs them.

```bash
python consumer/main.py
```

## Result

- The client sends `"Hello World!"` messages to the `tevs` queue.
- The consumer receives and prints them.

## Notes

- The queue used is named `tevs`.
- You can monitor messages using the RabbitMQ web UI.
