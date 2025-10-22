import asyncio

async def spam():
    while True:
        await asyncio.sleep(0)  # never yields long enough!

asyncio.run(spam())