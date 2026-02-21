from flask import Flask, render_template, request  # Flask basics and handling HTML rendering and request data
from flask_socketio import SocketIO, send          # Flask-SocketIO for WebSocket support
from datetime import datetime                      # Used for timestamping messages

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Secret key for session management

# Enable WebSocket support via Flask-SocketIO
socketio = SocketIO(app)

# ----------------------------
# Route for the homepage that renders the chat interface
# ----------------------------
@app.route('/')
def index():
    return render_template('chat.html')  # Loads chat UI from 'templates/chat.html'

# ----------------------------
# Handle incoming WebSocket messages from clients
# ----------------------------
@socketio.on('message')
def handleMessage(msg):
    # Get the client's IP address from the request
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        client_ip = request.environ['REMOTE_ADDR']  # Direct IP
    else:
        # If the app is behind a reverse proxy, use the X-Forwarded-For header
        client_ip = request.environ['HTTP_X_FORWARDED_FOR']

    # Get the current time for timestamping the message
    current_timestamp = datetime.now().strftime('%H:%M:%S')

    # Debug print in server terminal
    print('Message: ' + msg)

    # Format message with time and sender IP
    msg = f"{current_timestamp} Client {client_ip} wrote: {msg}"

    # Send the message to all connected clients
    send(msg, broadcast=True)

# ----------------------------
# Start the Flask + SocketIO server
# ----------------------------
if __name__ == '__main__':
    socketio.run(
        app,
        host='0.0.0.0',       # Accept connections from any network interface
        port=4001,            # Run on port 4001
        debug=True,
        allow_unsafe_werkzeug=True  # Only needed for dev/testing; unsafe in production
    )
