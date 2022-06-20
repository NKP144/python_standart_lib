import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('publisher')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"

# Make connection to the RabbitMQ server on local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

logger.debug(f"Send {severity} : {message} to direct_logs ")
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

logger.debug("Close RabbitMQ connection")
connection.close()
