import asyncio
import logging
from random import randint

from aiologger.loggers.json import JsonLogger
from aiologger.utils import CallableWrapper


def rand():
    return randint(1, 100)


logger = JsonLogger.with_default_handlers(level=logging.DEBUG)


async def main():

    # {"logged_at": "2022-06-15T20:28:42.047607+03:00", "line_number": 16, "function": "main", "level": "INFO",
    #  "file_path": "aiologger_callables.py", "msg": 55}
    await logger.info(CallableWrapper(rand))

    # {"logged_at": "2022-06-15T20:28:42.047696+03:00", "line_number": 17, "function": "main", "level": "INFO",
    #  "file_path": "aiologger_callables.py", "msg": {"Info message": 12}}
    await logger.info({"Info message": CallableWrapper(rand)})
    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
