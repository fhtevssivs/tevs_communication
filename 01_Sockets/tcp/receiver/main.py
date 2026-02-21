import socket  # Import the socket module to work with network connections

# Define server address and port number
# 'localhost' means the server will only be accessible from the same computer
server_address = ('localhost', 12345)

# Create a TCP/IP socket (SOCK_STREAM is used for TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port defined above
sock.bind(server_address)

# Start listening for incoming connections (max 1 connection in the queue)
sock.listen(1)
print('Starting up on {} port {}'.format(*server_address))

# Main loop: keeps the server running and accepting connections
while True:
    print('\nWaiting for a connection')

    # Accept a new connection from a client
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # Inner loop: receive data from the connected client
        while True:
            # Receive up to 4096 bytes of data from the client
            data = connection.recv(4096)

            # If no data is received, the client has closed the connection
            if not data:
                break

            # Decode and print the received data
            print('Received:', data.decode())

    # Always close the connection when done (even if there's an error)
    finally:
        connection.close()
