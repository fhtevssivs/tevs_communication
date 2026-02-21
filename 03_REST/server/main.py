import json
import logging
import random
import uuid
from datetime import datetime

from flask import Flask, render_template
from flask_cors import CORS  # Allows cross-origin requests (important for frontend/backend separation)
from flask_restful import Api, Resource, reqparse  # Used to easily create REST APIs with Flask

# Create the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing
api = Api(app)  # Create an API object to register resources

# Set up logging to display useful information in the console
logging.basicConfig(level=logging.INFO)

# ----------------------------
# Sample/mock data to simulate a database
# Each person has an ID, name, status, and timestamp
# ----------------------------
persons = [
    {"id": str(uuid.uuid4()), "name": "Alice", "status": "Ready for tasks", "last_status_update": str(datetime.now())},
    {"id": str(uuid.uuid4()), "name": "Bob", "status": "Busy with customer", "last_status_update": str(datetime.now())},
    {"id": str(uuid.uuid4()), "name": "Charlie", "status": "On Break", "last_status_update": str(datetime.now())},
]

# ----------------------------
# Person Resource: GET, PUT, DELETE individual persons
# ----------------------------
class Person(Resource):
    def get(self, person_id):
        # Look up a person by their UUID
        for person in persons:
            if person["id"] == str(person_id):
                return person, 200
        return "Person not found", 404

    def put(self, person_id):
        # Update or create a person
        logging.info(f"Received person_id: {person_id}")

        if person_id is None:
            person_id = str(uuid.uuid4())
        else:
            try:
                if not isinstance(person_id, uuid.UUID):
                    person_id = uuid.UUID(person_id)  # Validate UUID format
            except Exception:
                logging.exception(f"Invalid person_id: {person_id}")
                return "Invalid ID", 400

        # Parse the request data
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("status")
        args = parser.parse_args()

        if args["name"] is None or args["status"] is None:
            return "Name or Status arguments missing", 400

        # Update existing person if found
        for person in persons:
            if person["id"] == str(person_id):
                person["name"] = args["name"]
                person["status"] = args["status"]
                return person, 200

        # Create new person if not found
        person = {
            "id": str(person_id),
            "name": args["name"],
            "status": args["status"],
            "last_status_update": str(datetime.now())
        }
        persons.append(person)
        return person, 201

    def delete(self, person_id):
        # Delete a person by ID
        global persons
        persons = [person for person in persons if person["id"] != str(person_id)]
        return "", 204  # No content

# ----------------------------
# PersonList Resource: GET all, POST new
# ----------------------------
class PersonList(Resource):
    def get(self):
        return persons, 200

    def post(self):
        person_id = str(uuid.uuid4())

        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("status")
        args = parser.parse_args()

        if args["name"] is None or args["status"] is None:
            return "Name or Status arguments missing", 400

        person = {
            "id": person_id,
            "name": args["name"],
            "status": args["status"],
            "last_status_update": str(datetime.now())
        }
        persons.append(person)
        return person, 201

# Register resources to API
api.add_resource(PersonList, "/persons/")                  # For all persons
api.add_resource(Person, "/persons/<uuid:person_id>")      # For a specific person

# ----------------------------
# Extra RPC-like route: Return a random person
# ----------------------------
@app.route('/persons/getRandomPerson')
def getRandomPerson():
    if len(persons) > 0:
        return random.choice(persons)
    else:
        return "No person in status array", 404

# ----------------------------
# Default homepage route
# ----------------------------
@app.route('/')
def home():
    return render_template('client.html')  # Serves a frontend (HTML file)

# ----------------------------
# Start the server
# ----------------------------
if __name__ == "__main__":
    # Runs the app on all interfaces at port 3001
    app.run(debug=True, host='0.0.0.0', port=3001)
