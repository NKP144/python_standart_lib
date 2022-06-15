import asyncio
import logging
from aiologger.loggers.json import JsonLogger


async def main():
    logger = JsonLogger.with_default_handlers(
        level=logging.DEBUG,
        serializer_kwargs={'indent': 4}
    )

    await logger.info({
        "artist": "Black Community",
        "song": "Cold"
    })

    await logger.warning({'Serializer': 'Indent', 'Value': 4}, serializer_kwargs={'indent': 4})

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()



