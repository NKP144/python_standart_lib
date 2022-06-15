import logging

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('This message should appear to console')
logging.info('info message')
logging.warning('warning message')

