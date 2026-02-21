from datetime import datetime  # Used to get the current date and time
import socket  # Used to create and manage the network connection
import time  # Used to pause the program for a few seconds between messages

# Define the server address and port to connect to
server_address = ('localhost', 12345)

# Create a TCP/IP socket (SOCK_STREAM means TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using the address and port
sock.connect(server_address)
print('Connected to {} port {}'.format(*server_address))

try:
    # Keep sending messages to the server in a loop
    while True:
        # Create a message with the current time
        message = f"It's {datetime.now()}"

        # Print the message to the console
        print('Sending: {!r}'.format(message))

        # Send the message to the server (as bytes)
        sock.sendall(message.encode())

        # Wait for 5 seconds before sending the next message
        time.sleep(5)

# This block always runs at the end (even if there's an error or interruption)
finally:
    print('Closing socket')
    sock.close()  # Close the connection to the server
