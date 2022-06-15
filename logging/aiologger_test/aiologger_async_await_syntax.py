import asyncio
from aiologger import Logger


async def main():
    logger = Logger.with_default_handlers(name='my_aiologger')

    await logger.debug('debug at stdout')
    await logger.info('info at stdout')
    await logger.warning('warning at stderr')
    await logger.error('error at stderr')
    await logger.critical('critical at stderr')

    await logger.shutdown()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
