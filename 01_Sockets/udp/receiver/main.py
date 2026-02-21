import socket  # Import the socket module for network communication

# Define the server's address and port
# 'localhost' means it only listens for messages from the same machine
server_address = ('localhost', 12345)

# Create a UDP socket (SOCK_DGRAM indicates UDP protocol)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address so it can receive messages sent to that port
sock.bind(server_address)

print('Starting up on {} port {}'.format(*server_address))

# Infinite loop to keep the server running and receiving messages
while True:
    print('\nWaiting to receive message')

    # Wait for a message to arrive (max size 4096 bytes)
    # recvfrom returns both the data and the address of the sender
    data, address = sock.recvfrom(4096)

    # Print info about the received message
    print('Received {} bytes from {}'.format(len(data), address))

    # Decode and print the message contents (assuming it's UTF-8 text)
    print(data.decode())
