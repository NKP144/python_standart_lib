import asyncio
import logging
from aiologger.loggers.json import JsonLogger
from aiologger.formatters.json import FUNCTION_NAME_FIELDNAME, LOGGED_AT_FIELDNAME


async def main():
    logger = JsonLogger.with_default_handlers(
        level=logging.DEBUG,
        exclude_fields=[FUNCTION_NAME_FIELDNAME,
                        LOGGED_AT_FIELDNAME,
                        'file_path',
                        'line_number']
    )

    await logger.info("Function, file path and line number wont be printed")

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
