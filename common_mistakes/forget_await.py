import asyncio
async def greet():
    print("Hello")

async def main():
    greet()  # Missing await
    print("Done")

asyncio.run(main())