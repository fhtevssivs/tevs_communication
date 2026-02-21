import time  # Used to pause between sending messages
import pika  # Python client for RabbitMQ
import logging  # Used to print useful information to the console

# Configure logging output
logging.basicConfig(encoding='utf-8', level=logging.INFO)

# Infinite loop to keep sending messages every 5 seconds
while True:
    # Establish a connection to the RabbitMQ server running on localhost
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    # Open a communication channel
    channel = connection.channel()

    # Make sure the queue named 'tevs' exists (creates it if not)
    channel.queue_declare(queue='tevs')

    # Send a message to the 'tevs' queue
    channel.basic_publish(
        exchange='',          # Default exchange
        routing_key='tevs',   # Queue name (acts as the routing key)
        body='Hello World!'   # Message content
    )

    # Log a confirmation message to the console
    logging.info(" [x] Sent 'Hello World!!!!'")

    # Close the connection to RabbitMQ
    connection.close()

    # Wait for 5 seconds before sending the next message
    time.sleep(5)
