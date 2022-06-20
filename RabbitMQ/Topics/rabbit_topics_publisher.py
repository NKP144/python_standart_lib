import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('publisher')
facility_severity_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"

# Make connection to the RabbitMQ server on local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topics_logs',
                         exchange_type='topic')

logger.debug(f"Send {facility_severity_key} : {message} to direct_logs ")
channel.basic_publish(exchange='topics_logs',
                      routing_key=facility_severity_key,
                      body=message)


logger.debug("Close RabbitMQ connection")
connection.close()
