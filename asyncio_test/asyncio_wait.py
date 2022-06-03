import asyncio


async def phase(i):
    print(f'in phase {i}')
    # await asyncio.sleep(0.1 * i)
    for j in range(3):
        print(f'phase{i} = {j}')
        # time.sleep(1)
        await asyncio.sleep(1 * i)
    print(f'done with phase {i}')
    return f'phase {i} result'


async def main(num_phases):
    print('starting main')
    phases = [phase(i) for i in range(num_phases)]
    print('waiting for phases to complete')
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print(f'results: {results}')

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

