import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('publisher')
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Make connection to the RabbitMQ server on local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

logger.debug(f"Send {message} to RabbitMQ")
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

logger.debug("Close RabbitMQ connection")
connection.close()

