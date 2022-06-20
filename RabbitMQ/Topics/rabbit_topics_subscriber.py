import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('subscriber')
binding_keys = sys.argv[1:]
if not binding_keys:
    logger.error("Usage: %s [binding_keys]\n" % sys.argv[0])
    sys.stderr.write("Usage: %s [binding_keys]\n" % sys.argv[0])
    sys.exit(1)


def callback(ch, method, properties, body):
    logger.debug(f"Received from {method.routing_key}  msg:{body.decode()}")


def main():
    # Make connection to the RabbitMQ server on local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topics_logs',
                             exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    logger.debug(f"Queue name: {result.method.queue}")
    logger.debug(f"Binding_keys: {binding_keys}")

    for binding_key in binding_keys:
        channel.queue_bind(exchange='topics_logs',
                           queue=result.method.queue,
                           routing_key=binding_key)

    logger.debug("Waiting for logs with. To exit press CTRL+C")
    channel.basic_consume(queue=result.method.queue,
                          on_message_callback=callback,
                          auto_ack=True)

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
