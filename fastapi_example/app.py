# app.py
import time
import threading
from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio
from concurrent.futures import ThreadPoolExecutor



@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor(max_workers=10)
    loop.set_default_executor(executor)
    yield
    executor.shutdown(wait=True)

# uvicorn app:app --reload
app = FastAPI(lifespan=lifespan)

@app.get("/async")
async def async_endpoint():
    """Simulates a non-blocking async endpoint"""
    thread = threading.current_thread()
    print(f"🧱 [ASYNC] Handling request in name={thread.name}, id={thread.ident}")
    await asyncio.sleep(2)
    return {"endpoint": "async"}

@app.get("/sync")
def sync_endpoint():
    """Simulates a blocking sync endpoint"""
    thread = threading.current_thread()
    print(f"🧱 [SYNC] Handling request in name={thread.name}, id={thread.ident}")
    time.sleep(2)
    return {"endpoint": "sync"}

@app.get("/bad-async")
async def bad_async_endpoint():
    """Simulates a non-blocking async endpoint"""
    threading.current_thread()
    time.sleep(2)
    return {"endpoint": "bad-async"}

@app.get("/fast")
async def async_endpoint():
    """Simulates a non-blocking async endpoint"""
    await asyncio.sleep(0.1)
    return {"endpoint": "fast"}