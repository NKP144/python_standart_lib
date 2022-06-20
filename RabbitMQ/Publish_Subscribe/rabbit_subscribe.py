import sys
sys.path.append('../')

import os
import pika
import logger

logger = logger.create_logger('subscriber')


def callback(ch, method, properties, body):
    logger.debug(f"Received msg: {body.decode()}")
    print(" [x] %r" % body)


def main():
    # Make connection to the RabbitMQ server on local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             exchange_type='fanout')

    # 1. Random queue name
    # 2. Once the consumer connection is closed, the queue should be deleted
    result = channel.queue_declare(queue='', exclusive=True)
    logger.debug(f"Queue name: {result.method.queue}")

    channel.queue_bind(exchange='logs',
                   queue=result.method.queue)

    logger.debug("Waiting fir logs. To exit press CTRL+C")
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





