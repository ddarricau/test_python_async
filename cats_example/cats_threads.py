import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

os.makedirs("cats_threaded", exist_ok=True)

def fetch_cat(i):
    url = "https://cataas.com/cat"
    try:
        resp = requests.get(url, verify=False, timeout=10)
        if resp.status_code == 200:
            with open(f"cats_threaded/cat_{i}.jpg", "wb") as f:
                f.write(resp.content)
            print(f"🐱 Cat #{i} downloaded!")
        else:
            print(f"⚠️ Failed to fetch cat #{i}, status {resp.status_code}")
    except Exception as e:
        print(f"❌ Error fetching cat #{i}: {e}")


if __name__ == "__main__":
    start = time.perf_counter()
    MAX_WORKERS = 10
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(fetch_cat, i) for i in range(30)]
        for future in as_completed(futures):
            future.result()
    end = time.perf_counter()
    print(f"⏱️ Finished in {end - start:.2f} seconds using threads")