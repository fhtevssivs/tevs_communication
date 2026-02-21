import pika, sys, os  # pika = RabbitMQ client; sys and os used for clean shutdown
import logging  # For printing log messages

# Configure logging
logging.basicConfig(encoding='utf-8', level=logging.INFO)

def main():
    # Connect to RabbitMQ server running on localhost
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    # Open a communication channel
    channel = connection.channel()

    # Ensure the queue 'tevs' exists (safe even if it already exists)
    channel.queue_declare(queue='tevs')

    # Define what to do when a message is received
    def callback(ch, method, properties, body):
        logging.info(" [x] Received %r" % body)  # Log the received message

    # Register the callback to the 'tevs' queue
    channel.basic_consume(
        queue='tevs',              # Listen to this queue
        on_message_callback=callback,  # Use this function to handle messages
        auto_ack=True              # Automatically mark messages as "acknowledged"
    )

    logging.info(' [*] Waiting for messages. To exit press CTRL+C')

    # Start consuming (blocking loop)
    channel.start_consuming()

# Start the script
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
