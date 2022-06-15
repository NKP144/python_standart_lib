import asyncio
import logging
from aiologger.loggers.json import JsonLogger


async def main():
    # logger = JsonLogger.with_default_handlers(level=logging.DEBUG, flatten=True)
    logger = JsonLogger.with_default_handlers(level=logging.DEBUG)


    # {"logged_at": "2022-06-15T20:35:12.376305+03:00", "line_number": 11, "function": "main", "level": "INFO",
    #  "file_path": "aiologger_flatten.py", "status_code": 200, "response_time": 0.00534534}
    # await logger.info({"status_code": 200, "response_time": 0.00534534})
    await logger.info({"status_code": 200, "response_time": 0.00534534}, flatten=True)

    # {"logged_at": "2022-06-15T20:35:12.376411+03:00", "line_number": 15, "function": "main", "level": "ERROR",
    #  "file_path": "aiologger_flatten.py", "status_code": 404, "response_time": 0.00134534}
    # await logger.error({"status_code": 404, "response_time": 0.00134534})
    await logger.error({"status_code": 404, "response_time": 0.00134534}, flatten=True)

    # Overwrite keys tha are already present
    await logger.info({'logged_at': 'Yesterday'}, flatten=True)

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
