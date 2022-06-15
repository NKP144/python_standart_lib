import logging
import queue
import logging.handlers

que = queue.Queue(-1)
queue_handler = logging.handlers.QueueHandler(que)
handler = logging.StreamHandler()

listener = logging.handlers.QueueListener(que, handler)

root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(threadName)s: %(message)s')
handler.setFormatter(formatter)

listener.start()

root.warning('Look out')

listener.stop()
