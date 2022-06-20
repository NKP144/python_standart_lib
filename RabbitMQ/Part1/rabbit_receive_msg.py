import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('consumer')
logger.debug(f"{sys.path}")

# When pika receive msg this function will be callback
def callback(ch, method, properties, body):
    logger.debug(f"Received msg: {body}")


def main():
    # Make connection to the RabbitMQ server on local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Create queue
    channel.queue_declare(queue='hello')

    # Subscribe 'callback' function for receive msg for pika queue
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    logger.debug("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)







