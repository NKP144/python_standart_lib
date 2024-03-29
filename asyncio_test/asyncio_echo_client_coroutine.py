import asyncio
import logging
import sys

MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts.',
]

SERVER_ADDRESS = ('bnso.ydns.eu', 10000)
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
        reader, writer = await asyncio.open_connection(*address)
    except OSError as e:
        log.debug(f'OSError: {e}')
        return

    for msg in messages:
        writer.write(msg)
        log.debug('sendind {!r}'.format(msg))
    if writer.can_write_eof():
        writer.write_eof()
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
