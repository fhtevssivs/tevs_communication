from datetime import datetime  # Used to get the current date and time
import socket  # Needed to create and use network sockets
import time  # Used to pause between sending messages

# Define the server address and port to send messages to
server_address = ('localhost', 12345)

# Loop forever to send a message every 5 seconds
while True:
    # Create a new UDP socket (SOCK_DGRAM means it's UDP, not TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Create a message that includes the current timestamp
        message = f"It's {datetime.now()}"

        # Print what is being sent (helpful for debugging or monitoring)
        print('Sending {!r}'.format(message))

        # Send the message as bytes to the server
        sock.sendto(message.encode(), server_address)

    # The finally block is always run, even if an error occurs
    finally:
        # Close the socket after sending the message
        print('Closing socket')
        sock.close()

    # Wait 5 seconds before sending the next message
    time.sleep(5)
