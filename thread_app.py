# app.py
import time
import threading
from fastapi import FastAPI
import asyncio

# uvicorn thread_app:app --reload
app = FastAPI()


# hey -n 10 -c 10 http://127.0.0.1:8000/sync
@app.get("/sync")
def sync_endpoint():
    """Simulates a blocking sync endpoint"""
    thread = threading.current_thread()
    print(f"🧱 [SYNC] Handling request in name={thread.name}, id={thread.ident}")
    time.sleep(2)
    return {"endpoint": "sync"}

# hey -n 10 -c 10 http://127.0.0.1:8000/async
@app.get("/async")
async def async_endpoint():
    """Simulates a non-blocking async endpoint"""
    thread = threading.current_thread()
    print(f"🧱 [SYNC] Handling request in name={thread.name}, id={thread.ident}")
    await asyncio.sleep(2)
    return {"endpoint": "async"}