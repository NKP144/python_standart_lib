import glob
import logging
import logging.handlers

LOG_FILENAME = "logging_rotatingfile.out"

# Создать регистратор с требуемым порогом важности сообщений
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Добавить в регистратор обработчик протоколируемых сообщений
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    backupCount=5
)
my_logger.addHandler(handler)

# Записать сообщение в журнал
for i in range(20):
    my_logger.debug(f'i = {i}')

# Вывести список созданных файлов
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)
