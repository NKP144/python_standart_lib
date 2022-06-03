import asyncio
import functools

def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


async def main(loop):
    # Создать и получить разделяемую блокировку
    event = asyncio.Event()
    print(f'event start state: {event.is_set()}')

    loop.call_later(0.1, functools.partial(set_event, event))

    print('waiting for coroutines')
    await asyncio.wait([coro1(event), coro2(event)])

    print(f'event end state: {event.is_set()}')


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
