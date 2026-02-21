# How to Start the REST API Demoserver

This project demonstrates a basic REST API server including a simple web frontend to access and interact with data exposed via the API.

---

## Step 1 (Option A): Start REST API Demoserver in Docker

> Use this option if you want to run the REST API Demoserver inside a Docker container.

Make sure Docker and Docker Compose are installed.

Start the REST API Demoserver with:

```bash
docker-compose -f docker-compose.yml up -d
```

---

## Step 1 (Option B): Start REST API Demoserver with Python

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

## Step 2: Open the Web Interface

Open your web browser and go to:
http://localhost:3001


You will see the web frontend connected to the REST API.  
You can also test the API directly using tools like **Postman**, **curl**, or your browser (for GET endpoints).

---

## Notes

- The API follows a RESTful structure and exposes endpoints for managing "person" objects.
- Data is stored in-memory (mocked list) and resets on server restart.
- The web frontend (`client.html`) is rendered from Flask using `render_template`.
- You can fetch a random person at `/persons/getRandomPerson`.
- Example endpoints:
  - `GET /persons/`
  - `POST /persons/`
  - `GET /persons/<uuid>`
  - `PUT /persons/<uuid>`
  - `DELETE /persons/<uuid>`

---
