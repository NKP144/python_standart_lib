import asyncio
from datetime import datetime
from aiologger.loggers.json import JsonLogger


async def main():
    logger = JsonLogger.with_default_handlers()
    # {"logged_at": "2022-06-15T17:27:20.574627+03:00", "line_number": 8, "function": "main", "level": "INFO",
    # "file_path": "aiologger_json.py", "msg": "A string"}
    await logger.info("A string")

    # {"logged_at": "2022-06-15T17:27:20.574726+03:00", "line_number": 10, "function": "main", "level": "INFO",
    #  "file_path": "aiologger_json.py",
    #  "msg": {"data_objects": "2022-06-15T17:27:20.574694", "exceptions": "Exception: KeyError('KeyError')",
    #          "types": "<class 'aiologger.loggers.json.JsonLogger'>"}}
    await logger.info({
        'data_objects': datetime.now(),
        'exceptions': KeyError("KeyError"),
        'types': JsonLogger
    })

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

