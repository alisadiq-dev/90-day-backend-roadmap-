# Day 18 – Async Programming in FastAPI

Today I learned **async programming** and made my FastAPI app handle multiple requests at the same time!

### What I Did
- Created sync and async endpoints
- Used `await asyncio.sleep()` to simulate slow operations
- Made async external API call with `httpx.AsyncClient()`
- Demonstrated concurrency (3 slow tasks finish in ~2 seconds instead of 6)

### Key Concepts
- `async def` → makes function non-blocking
- `await` → waits without blocking the server
- Async is perfect for I/O operations (database, API calls)
- Sync blocks the server – bad for many users

### How to Run
```bash
uvicorn src.main:app --reload