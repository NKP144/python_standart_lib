import requests
import time
from concurrent.futures import ProcessPoolExecutor
import asyncio, aiohttp
from aiohttp import ClientSession, ClientResponseError
import urllib.request

# EXAMPLE 1
# #Multithreading ---------------------------------------------------------------
# def fetch_url_data(pg_url):
#     try:
#         resp = requests.get(pg_url)
#     except Exception as e:
#         print(f"Возникла ошибка при получении данных из url: {pg_url}")
#     else:
#         return resp.content
#
#
# def get_all_url_data(url_list):
#     with ProcessPoolExecutor() as executor:
#         resp = executor.map(fetch_url_data, url_list)
#     return resp
#
#
# if __name__ == '__main__':
#     url = "https://www.uefa.com/uefaeuro-2020/"
#     for ntimes in [1, 10, 50, 100, 500]:
#         start_time = time.time()
#         responses = get_all_url_data([url] * ntimes)
#         print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')


# async def fetch_url_data(session, url):
#     try:
#         async with session.get(url, timeout=60) as response:
#             resp = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return resp
#     return
#
#
# async def fetch_async(loop, r):
#     url = "https://www.uefa.com/uefaeuro-2020/"
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session, url))
#             tasks.append(task)
#         responses = await asyncio.gather(*tasks)
#     return responses
#
#
# if __name__ == '__main__':
#     for ntimes in [1, 10, 50, 100, 500]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(fetch_async(loop, ntimes))
#         # будет выполняться до тех пор, пока не завершится или не возникнет ошибка
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')


# EXAMPLE 2

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def fetch_sync(pid):
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    return datetime


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp.request('GET', URL)
    datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


print('Synchronous:')
synchronous()

print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()