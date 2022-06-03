import asyncio


async def phase1():
    print(f'in phase1')
    await asyncio.sleep(2)
    print(f'done with phase1')
    return f'phase1 result'


async def phase2():
    print(f'in phase2')
    await asyncio.sleep(1)
    print(f'done with phase2')
    return f'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    results = await asyncio.gather(phase1(), phase2())
    print(f'results: {results}')

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main())
finally:
    event_loop.close()

