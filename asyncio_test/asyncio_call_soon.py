import asyncio
import functools
import time


# def callback(arg, *, kwarg='default'):
#     print('callback invoked with {} and {}'.format(arg, kwarg))

def callback(arg, kwarg='default'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    # wrapped = functools.partial(callback, kwarg='not default')
    # loop.call_soon(wrapped, 2)
    loop.call_soon(callback, 2, 'not default')

    # await asyncio.sleep(0.1)
    await phase_coroutine1()


async def phase_coroutine1():
    print('in phase1')
    for i in range(5):
        print(f'phase1 = {i}')
        # time.sleep(1)
        await asyncio.sleep(1)
    return 'phase1 finish'


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()

