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
    condition1 = asyncio.Condition()
    condition2 = asyncio.Condition()

    # Создать список задач, отслеживающих условие
    consumers1 = [consumer(condition1, i) for i in range(5)]
    consumers2 = [consumer(condition2, i) for i in range(5)]
    # consumers = consumers1 + consumers2
    tasks = consumers1 + consumers2

    # Запланировать задачу для манипулирования переменной condition (условием)
    # man_task1 = loop.create_task(manipulate_condition(condition1))
    # man_task2 = loop.create_task(manipulate_condition(condition2))
    # print(f'{man_task1}, {man_task2}')

    tasks.append(loop.create_task(manipulate_condition(condition1)))
    tasks.append(loop.create_task(manipulate_condition(condition2)))

    # Запустить сопрограммы, которые ждут условий
    # await asyncio.wait(consumers)
    await asyncio.wait(tasks)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
