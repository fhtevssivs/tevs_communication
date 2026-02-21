# How to Start the JSON-RPC Demoserver

This project demonstrates a basic **JSON-RPC server and client setup** using Python.

---

## Step 1: Start JSON-RPC Demoserver with Python

Install the required dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python server/main.py
```

This will launch a JSON-RPC 2.0 compliant server on:

```
http://localhost:2000/
```

---

## Step 2: Start JSON-RPC Democlient with Python

> Note: If you haven't already installed the dependencies in Step 1, do so before proceeding.

Run the client:

```bash
python client/main.py
```

The client will send a JSON-RPC request (e.g. `add(a=10, b=10)`) to the server and print the result.

---

## Optional: Test with Postman

You can also use **Postman** (or any HTTP client) to manually send a JSON-RPC request:

- Set method to `POST`
- URL: `http://localhost:2000/`
- Headers:
  ```
  Content-Type: application/json
  ```
- Body (raw, JSON):
  ```json
  {
    "jsonrpc": "2.0",
    "method": "add",
    "params": { "a": 10, "b": 10 },
    "id": 1
  }
  ```

---

## Notes

- This setup uses HTTP POST with `application/json` headers to communicate.
- JSON-RPC is a lightweight alternative to REST for structured remote procedure calls.
- You can easily extend the server by adding new methods using the `@method` decorator from `jsonrpcserver`.

---
