import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coro1(lock):
    print('coro1 waiting for the lock')
    # with await lock:
    async with lock:
        print('coro1 acquired lock')
        await asyncio.sleep(1)
    print('coro1 released lock')


async def coro2(lock):
    print('coro2 waiting for the lock')
    # await lock
    async with lock:
        try:
            print('coro2 acquired lock')
            await asyncio.sleep(1)
        finally:
            print('coro2 released lock')
            # lock.release()


async def main(loop):
    # Создать и получить разделяемую блокировку
    lock = asyncio.Lock()
    print('acquiring the lock')
    await lock.acquire()
    print(f'lock acquired: {lock.locked()}')

    # Запланировать callback для отмены блокировки
    loop.call_later(0.1, functools.partial(unlock, lock))

    # Запустить сопрограммы, которые хотят использовать блокировку
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)])


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
