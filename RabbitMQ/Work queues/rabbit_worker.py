import sys
sys.path.append('../')

import os
import pika
import logger
import time

logger = logger.create_logger('consumer')


# When pika receive msg this function will be callback
def callback(ch, method, properties, body):
    logger.debug(f"Received msg: {body.decode()}")
    logger.debug(f"Sleep for {body.count(b'.')}")
    time.sleep((body.count(b'.')))
    logger.debug("Done")

    # Add manual ACK sending
    logger.debug("Send ACK")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    # Make connection to the RabbitMQ server on local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Create queue
    # channel.queue_declare(queue='hello')
    # Пометить очередь как надёжную, в случае проблем с сервером RabbitMQ
    # сообщения в очереди сохраняться
    channel.queue_declare(queue='task_queue', durable=True)


    # Subscribe 'callback' function for receive msg for pika queue
    # channel.basic_consume(queue='hello',
    #                       auto_ack=True,
    #                       on_message_callback=callback)

    # Queue size
    channel.basic_qos(prefetch_count=1)
    # Delete auto_ack flag
    channel.basic_consume(queue='task_queue',
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
