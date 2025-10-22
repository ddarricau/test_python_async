from fastapi import FastAPI
import time
import asyncio

# uvicorn app:app --reload
app = FastAPI()

# hey -n 100 -c 100 http://127.0.0.1:8000/sync
@app.get("/sync")
def slow_sync():
    """Simulates a slow blocking operation."""
    time.sleep(2)
    return {"status": "done", "type": "sync"}

# hey -n 100 -c 100 http://127.0.0.1:8000/async
@app.get("/async")
async def slow_async():
    """Simulates a slow async operation."""
    await asyncio.sleep(2)
    return {"status": "done", "type": "async"}