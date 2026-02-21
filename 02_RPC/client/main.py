import requests  # Used to make HTTP requests
import json      # Used to work with JSON data

# Define a function to send a JSON-RPC request
def json_rpc(url, id=1):
    # Set the header to tell the server we're sending JSON
    headers = {'Content-Type': 'application/json'}

    # Create the JSON-RPC request payload
    payload = {
        "jsonrpc": "2.0",        # JSON-RPC protocol version
        "method": "add",         # The name of the method we want to call on the server
        "params": {"a": 10, "b": 10},  # Parameters for the method
        "id": 2                  # Unique ID for this request (used to match response)
    }

    # Send the request to the server using HTTP POST
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Convert the JSON response to a Python dictionary and return it
    return response.json()

# Call the json_rpc function with the server URL
response = json_rpc("http://localhost:2000/")

# Print the response from the server
print(response)
