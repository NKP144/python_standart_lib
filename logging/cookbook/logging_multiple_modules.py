import logging
import logging_auxiliary

# create logget with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to tha handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of logging_auxiliary.Auxiliary')
a = logging_auxiliary.Auxiliary()
logger.info('created an instance of logging_auxiliary.Auxiliary')
logger.info('calling logging_auxiliary.Auxiliary.do_something')
a.do_something()
logger.info('finished logging_auxiliary.Auxiliary.do_something')
logger.info('calling logging_auxiliary.some_function()')
logging_auxiliary.some_function()
logger.info('done with logging_auxiliary.some_function()')
logger.error('console error testing ')


