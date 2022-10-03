import asyncio
import time

start = time.time()


async def foo():
    print('Started foo {}'.format(tic()))
    await asyncio.sleep(3)
    print('Ended in foo {}'.format(tic()))


async def bar():
    print('Started bar {}'.format(tic()))
    await asyncio.sleep(3)
    print('Ended bar {}'.format(tic()))


async def gr():
    for i in range(3):
        print('Some work in gr {}'.format(tic()))
        await asyncio.sleep(1)
        print('Ended gr')


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


event_loop = asyncio.get_event_loop()
tasks = [
    event_loop.create_task(foo()),
    event_loop.create_task(bar()),
    event_loop.create_task(gr())
]

if __name__ == "__main__":
    try:
        event_loop.run_until_complete(asyncio.wait(tasks))
        event_loop.close()
    except:
        pass
