import asyncio


async def consumer(condition, n):
    # with await condition:
    async with condition:
        print(f'consumer {n} is waiting')
        await condition.wait()
        print(f'consumer {n} triggered')
    print(f'ending consumer {n}')


async def manipulate_condition(condition):
    print('starting manipulate_condition')

    # Пауза для запуска источников ожидающих сигналы
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        # with await condition:
        async with condition:
            print(f'notifying {i} consumers')
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    # with await condition:
    async with condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending manipulate_condition')


async def main(loop):
    # Создать условие
    condition = asyncio.Condition()

    # Создать список задач, отслеживающих условие
    consumers = [consumer(condition, i) for i in range(5)]

    # Запланировать задачу для манипулирования переменной condition (условием)
    loop.create_task(manipulate_condition(condition))

    # Запустить сопрограммы, которые ждуи условий
    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
