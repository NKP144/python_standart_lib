import asyncio
# import logging
from aiologger import Logger


async def main():
    # logger = logging.getLogger(__name__)
    logger = Logger.with_default_handlers(name='my_aiologger')
    # logging.basicConfig(level=logging.DEBUG, format="%(message)s")

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

    await logger.shutdown()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
