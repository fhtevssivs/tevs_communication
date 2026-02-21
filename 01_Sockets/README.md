# How to Start the TCP and UDP Sender-Receiver Demo

This project demonstrates simple examples of TCP and UDP communication using Python — including a sender and a receiver for each protocol.

---

## TCP Sender & Receiver

### Step 1: Start the TCP Receiver

Run the receiver first so it can listen for incoming messages:

```bash
python tcp/receiver/main.py
```

### Step 2: Start the TCP Sender

In a separate terminal:

```bash
python tcp/sender/main.py
```

The TCP sender will connect to the receiver and send periodic messages.

---

## UDP Sender & Receiver

### Step 1: Start the UDP Receiver

Run the receiver to listen for incoming datagrams:

```bash
python udp/receiver/main.py
```

### Step 2: Start the UDP Sender

In a separate terminal:

```bash
python udp/sender/main.py
```

The UDP sender will send datagrams to the receiver every few seconds.

---

## Notes

- These examples use Python’s built-in `socket` module.
- No external dependencies are required.
- TCP provides reliable, ordered delivery.
- UDP is connectionless and lightweight.
