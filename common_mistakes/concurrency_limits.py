import asyncio
import aiohttp
import ssl
import time

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


CONCURRENCY_LIMIT = 2
sem = asyncio.Semaphore(CONCURRENCY_LIMIT)



async def fetch_url_safe(session: aiohttp.ClientSession, url: str):
    """
    Fetch a URL with concurrency control via a semaphore.
    """
    async with sem:
        print(f"[SAFE] Fetching {url}")
        async with session.get(url, ssl=ssl_context) as response:
            img = await response.read()
            print(f"[UNSAFE] Done: {url} (status {response.status})")
            return img

async def fetch_url(session: aiohttp.ClientSession, url: str):
    """
    Fetch a URL with concurrency control via a semaphore.
    """
    print(f"[UNSAFE] Fetching {url}")
    async with session.get(url, ssl=ssl_context) as response:
        img = await response.read()
        print(f"[UNSAFE] Done: {url} (status {response.status})")
        return img


async def main():
    """
    Create a limited number of concurrent fetches.
    """
    URLS = [f"https://cataas.com/cat" for _ in range(40)]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in URLS]
        results = await asyncio.gather(*tasks)
        print(f"Retrieved {len(results)} pages total.")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"⏱️ Finished in {end - start:.2f} seconds")
