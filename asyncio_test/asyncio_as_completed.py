import asyncio


async def phase(i):
    print(f'in phase {i}')
    await asyncio.sleep(0.5 - (0.1 * i))
    print(f'done with phase {i}')
    return f'phase {i} result'


async def main(num_phases):
    print('starting main')
    phases = [phase(i) for i in range(num_phases)]
    print('waiting for phases to complete')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        results.append(answer)
    print(f'results: {results}')
    return results

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

