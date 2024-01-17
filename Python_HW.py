
import aiohttp
import asyncio
import time

async def get_json(session,i):
    async with session.get(f"https://jsonplaceholder.typicode.com/posts/{i}") as response:
        return await response.text()

s = time.perf_counter()
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1,101):
            task = get_json(session,i)
            tasks.append(task)
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    res = asyncio.run(main())
    e = time.perf_counter()
    for i in res:
        print(i)

    print(e - s)
