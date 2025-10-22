import asyncio

async def say_hi():
    print("👋 hi there")
    await asyncio.sleep(1)
    print("bye!")

async def main():
    say_hi()  # forgot to await!
    await asyncio.sleep(2)

asyncio.run(main())