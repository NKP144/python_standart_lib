import asyncio


async def consumer(n, q):
    print(f'consumer {n}: starting')
    while True:
        print(f'consumer {n}: waiting for item')
        item = await q.get()
        print(f'consumer {n}: has item {item}')
        if item is None:
            # None - сигнал прекратить выполнение
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()

    print(f'consumer {n}: ending')


async def producer(q, num_workers):
    print('producer: starting')
    # Добавить некоторое количество элементов в очередь
    for i in range(num_workers * 3):
        await q.put(i)
        print(f'producer: added task {i} to the queue')

    # Добавить в очередь несколько элементов None для прекращения выполения действий на приёмной стороне
    for i in range(num_workers):
        await q.put(None)
        print(f'producer: waiting for queue to empty')
        await q.join()
        print('producer: ending')


async def main(loop, num_consumers):
    # Создать очередь фиксированного размера
    q = asyncio.Queue(maxsize=num_consumers)

    # Запланировать задачи приёмники
    consumers = [loop.create_task(consumer(i, q)) for i in range(num_consumers)]

    # Запланировать задачи передатчики
    prod = loop.create_task(producer(q, num_consumers))

    # Ждать завершения работы всех сопрограмм
    await asyncio.wait(consumers + [prod])

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    result = event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()
