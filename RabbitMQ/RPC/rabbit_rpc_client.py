import sys
sys.path.append('../')

import os
import pika
import logger
import uuid


class FibonacciPpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        # Создать очередь для отправки задач серверу
        result = self.channel.queue_declare(queue='rpc-queue')
        self.rpc_queue = result.method.queue

        # Создать очередь для приема ответов от сервера
        reply_to_queue = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = reply_to_queue.method.queue
        logger.debug(f"reply_to: {self.callback_queue}")

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, properties, body):
        logger.debug(f"Response: correlation_id = {properties.correlation_id}")
        logger.debug(f"Response: body = {body}")
        if self.coord_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.coord_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.coord_id,
            ),
            body=str(n)
        )
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


logger = logger.create_logger('rpc_client')

fibonacci_rpc = FibonacciPpcClient()
result = fibonacci_rpc.call(4)
logger.debug("fib(4) is %r" % result)


