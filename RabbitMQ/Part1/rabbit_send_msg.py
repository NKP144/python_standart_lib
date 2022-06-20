import sys
sys.path.append('../')

import pika
import logger


logger = logger.create_logger('publisher')

# Make connection to the RabbitMQ server on local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue
channel.queue_declare(queue='hello')

# Send message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

logger.debug("Send 'Hello World to RabbitMQ")

connection.close()
logger.debug("Close RabbitMQ connection")

