import aiohttp, asyncio, os, ssl, time

os.makedirs("cats_async", exist_ok=True)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def fetch_cat(session, i):
    async with session.get("https://cataas.com/cat", ssl=ssl_context) as resp:
        img = await resp.read()
        with open(f"cats_example/cats_async/cat_{i}.jpg", "wb") as f:
            f.write(img)
        print(f"🐱 Cat #{i} downloaded!")

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(fetch_cat(session, i) for i in range(30)))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"⏱️ Finished in {end - start:.2f} seconds")