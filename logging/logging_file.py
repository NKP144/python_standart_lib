import logging

LOG_FILENAME = "logging_output.out"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)