from fastapi import FastAPI
from typing import List
import asyncio
import httpx

app = FastAPI(title="Day 18 - Async FastAPI Demo")

# normal sync route 
@app.get("/sync-slow")
def sync_slow():
    asyncio.sleep(2)
    return {"message": "Sync slow endpoint completed after 2 seconds"}
    
# async route 
@app.get("/async-slow")
async def async_slow():
    await asyncio.sleep(2)
    return {"message": "Async slow endpoint completed after 2 seconds"}
    
# real word example 
@app.get("/external-data")
async def external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()
        return {"title": data["title"], "body": data["body"][:100] + "..."}
    

# demo 
@app.get("/demo")
async def demo():
    task1 = asyncio.create_task(async_slow(2))
    task2 = asyncio.create_task(async_slow(2))
    task3 = asyncio.create_task(async_slow(2))
    
    await task1
    await task2
    await task3

    return {"message": "All tasks completed in 2 second not 6 second"}
