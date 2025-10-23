import asyncio
async def greet():
    print("Hello")

async def main():
    asyncio.run(greet())
    print("Done")

asyncio.run(main())