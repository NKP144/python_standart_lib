import asyncio

from aiologger import Logger
from aiologger.levels import LogLevel
from aiologger.handlers.files import AsyncTimedRotatingFileHandler, RolloverInterval
from aiologger.formatters.base import Formatter

import os
from aiologger.utils import get_running_loop
from typing import List


class FixedAsyncTimedRotatingFileHandler(AsyncTimedRotatingFileHandler):
    """
    FIXED AsyncTimedRotatingFileHandler
    """
    async def get_files_to_delete(self) -> List[str]:
        """
        Determine the files to delete when rolling over.
        """
        dir_name, base_name = os.path.split(self.absolute_file_path)
        loop = get_running_loop()
        file_names = await loop.run_in_executor(
            None, lambda: os.listdir(dir_name)
        )
        result = []
        prefix = base_name + "."
        plen = len(prefix)
        for file_name in file_names:
            if file_name[:plen] == prefix:
                suffix = file_name[plen:]
                if self.ext_match.match(suffix):
                    result.append(os.path.join(dir_name, file_name))
        if len(result) < self.backup_count:
            return []
        else:
            """
                THIS IS FIX
            """
            #result.sort(reverse=True)
            result.sort()  # os.listdir order is not defined
            return result[: len(result) - self.backup_count]


def create_logger(loop, config_debug=True):
    """
    """
    if loop is None:
        loop = asyncio.get_event_loop()
    formatter = Formatter('%(asctime)s - %(message)s')
    logger = Logger.with_default_handlers(loop=loop, formatter=formatter)

    h = FixedAsyncTimedRotatingFileHandler(
        filename='{}/error.log'.format(os.environ.get('LOGS_DIR', './logs')),
        when=RolloverInterval.DAYS,
        backup_count=int(os.environ.get('LOG_DAYS', '30')),
    )
    h.formatter = formatter
    h._level = LogLevel.ERROR
    logger.add_handler(h)

    if config_debug:
        h = FixedAsyncTimedRotatingFileHandler(
            filename='{}/debug.log'.format(os.environ.get('LOGS_DIR', './logs')),
            when=RolloverInterval.DAYS,
            backup_count=int(os.environ.get('LOG_DAYS', '30')),
        )
        h.formatter = formatter
        h._level = LogLevel.DEBUG
        logger.add_handler(h)
    return logger


async def main(loop):
    logger = create_logger(loop=loop)
    await logger.debug('Start loop')
    await logger.info('Info message')
    await logger.error('ERROR message')
    await logger.shutdown()


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

