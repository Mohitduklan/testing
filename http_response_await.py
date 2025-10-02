import aiohttp
import asyncio
import time
urls = ['https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently',
        'https://en.wikipedia.org/wiki/Grosswangen',
        'https://en.wikipedia.org/wiki/Green_Party_of_Switzerland',
        'https://en.wikipedia.org/wiki/National_Council_(Switzerland)',
        'https://en.wikipedia.org/wiki/Census_in_Switzerland']


async def get_http_res(session: aiohttp.ClientSession, url):
    async with session.get(url) as resp:
        text = await resp.text()
        return url, len(text)


async def main():
    now = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(get_http_res(session, url)) 
        
        for t in asyncio.as_completed(tasks):
            print(await t)
    then = time.time()
    print(then-now)
asyncio.run(main())