import sys
sys.path.append('../')

import pika
import logger


logger = logger.create_logger('publisher')

message = ' '.join(sys.argv[1:]) or "Hello World!"

# Make connection to the RabbitMQ server on local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue
# channel.queue_declare(queue='hello')
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='',
                      # routing_key='hello',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

logger.debug(f"Send {message} to RabbitMQ")

connection.close()
logger.debug("Close RabbitMQ connection")
