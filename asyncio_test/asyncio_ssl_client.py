import asyncio
import logging
import sys
import ssl

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.check_hostname = False
ssl_context.load_verify_locations('../ssl/pymotw.crt')

MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts.',
]

SERVER_ADDRESS = ('bnso.ydns.eu', 443)
#SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')


async def echo_client(address, messages):
    log = logging.getLogger('echo client')
    log.debug('connecting to {} port {}'.format(*address))

    try:
        log.debug('trying connected to server')
        reader, writer = await asyncio.open_connection(*address, ssl=ssl_context)
    except OSError as e:
        log.debug(f'OSError: {e}')
        return

    for msg in messages:
        writer.write(msg)
        log.debug('sendind {!r}'.format(msg))
    # SSL не поддерживает метке EOF, поэтому для обозначения
    # конца сообщения используется нулевой байт
    writer.write(b'\x00')
    await writer.drain()

    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('receiver {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return

event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(echo_client(SERVER_ADDRESS, MESSAGES))
finally:
    log.debug('closing event loop')
    event_loop.close()
