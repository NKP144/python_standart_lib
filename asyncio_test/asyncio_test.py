import asyncio
import time


async def main_coroutine():
    print('in main coroutine')
    print('waiting for phase1')
    result1 = await phase_coroutine1()
    print('waiting for phase2')
    result2 = await phase_coroutine2()
    return result1, result2


async def coroutine(number):
    print(f'in coroutine #{number}')
    return f'coroutine #{number} finish'
    # for i in range(5):
    #     print(f'coroutine #{number} = {i}')
    #     time.sleep(3)


async def phase_coroutine1():
    print('in phase1')
    for i in range(5):
        print(f'phase1 = {i}')
        # time.sleep(1)
        await asyncio.sleep(1)
    return 'phase1 finish'


async def phase_coroutine2():
    print('in phase2')
    for i in range(3):
        print(f'phase2 = {i}')
        # time.sleep(3)
        await asyncio.sleep(3)

    return 'phase2 finish'


event_loop = asyncio.get_event_loop()

try:
    print('starting process')
    # phase1 = phase_coroutine1()
    # phase2 = phase_coroutine2()
    main_coro = main_coroutine()
    return_value = event_loop.run_until_complete(main_coro)
    # event_loop.run_until_complete(coro2)
    print(return_value)
finally:
    print('closing event loop')
    event_loop.close()