import asyncio, time

async def bad_sleep():
    time.sleep(5)  # Blocks the event loop
    # await asyncio.sleep(5) # correct
    print("Done")

asyncio.run(bad_sleep())