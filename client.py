import httpx, asyncio, time

async def hit(client, path):
    start = time.perf_counter()
    r = await client.get(f"http://127.0.0.1:8000/{path}", timeout=10)
    print(f"{path}: {r.json()} in {time.perf_counter() - start:.2f}s")

async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            hit(client, "slow-sync"),
            hit(client, "fast"),
        )
        # await asyncio.gather(
        #     hit(client, "slow-async"),
        #     hit(client, "fast"),
        # )

asyncio.run(main())