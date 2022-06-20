import sys
sys.path.append('../')

import pika
import logger


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, properties, body):
    n = int(body)
    logger.debug(f"Request int = {n}")
    response = fib(n)
    logger.debug(f"Response fib = {response}")
    logger.debug(f"Replay_to = {properties.reply_to}")
    logger.debug(f"Correlation_id = {properties.correlation_id}")

    # sends a message with the result back to the client, using the queue from the reply_to field
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=str(response)
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)


logger = logger.create_logger('rpc_server')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создать очередь для отправки задач серверу
rpc_queue = channel.queue_declare(queue='rpc_queue')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

logger.debug("Awaiting RPC requests")
channel.start_consuming()



