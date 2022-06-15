import asyncio
import logging
from aiologger.loggers.json import JsonLogger


# async def main():
#     a = 69
#     b = 666
#     c = [a, b]
#
#     logger = JsonLogger.with_default_handlers(level=logging.DEBUG)
#
#     await logger.info("Simple log")
#
#     # {"logged_at": "2022-06-15T20:57:10.365410+03:00", "line_number": 14, "function": "main", "level": "INFO",
#     #  "file_path": "aiologger_extra.py", "msg": {"key": "value"}, "a": 69, "b": 666, "c": [69, 666],
#     #  "logger": "<aiologger.loggers.json.JsonLogger object at 0x7f98300c1d30>"}
#     await logger.info({"key": "value"}, extra=locals())
#     await logger.shutdown()

# # Override default content
# async def main():
#     logger = JsonLogger.with_default_handlers(level=logging.DEBUG)
#
#     await logger.info("I'm a simple log")
#     # {"msg": "I'm a simple log", "logged_at": "2017-08-11T12:21:05.722216", "line_number": 6, "function": "<module>", "level": "INFO", "path": "/Users/diogo/PycharmProjects/aiologger/bla.py"}
#
#     await logger.info("I'm a simple log", extra={'logged_at': 'Yesterday'})
#     # {"msg": "I'm a simple log", "logged_at": "Yesterday", "line_number": 6, "function": "<module>", "level": "INFO", "path": "/Users/diogo/PycharmProjects/aiologger/bla.py"}
#
#     await logger.shutdown()

async def main():
    logger = JsonLogger.with_default_handlers(level=logging.DEBUG, extra={'logged_at': 'Yesterday'})

    await logger.info("I'm a simple log")
    # {"msg": "I'm a simple log", "logged_at": "Yesterday", "line_number": 6, "function": "<module>", "level": "INFO", "path": "/Users/diogo/PycharmProjects/aiologger/bla.py"}

    await logger.info("I'm a simple log")
    # {"msg": "I'm a simple log", "logged_at": "Yesterday", "line_number": 6, "function": "<module>", "level": "INFO", "path": "/Users/diogo/PycharmProjects/aiologger/bla.py"}

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
