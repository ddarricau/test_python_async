import requests, os, time

os.makedirs("cats_sync", exist_ok=True)

def fetch_cat(i):
    url = "https://cataas.com/cat"
    # disable SSL verification (similar to your aiohttp ssl_context hack)
    resp = requests.get(url, verify=False)
    if resp.status_code == 200:
        with open(f"cats_example/cats_sync/cat_{i}.jpg", "wb") as f:
            f.write(resp.content)
        print(f"🐱 Cat #{i} downloaded!")
    else:
        print(f"⚠️ Failed to fetch cat #{i}, status {resp.status_code}")

if __name__ == "__main__":
    start = time.perf_counter()
    for i in range(30):
        fetch_cat(i)
    end = time.perf_counter()
    print(f"⏱️ Finished in {end - start:.2f} seconds")