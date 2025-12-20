# Day 18: Async Programming in Python & FastAPI

Today I learned async programming in Python and how it makes FastAPI super fast with many users.

## What is Async?
- **Normal (sync)** functions do one thing at a time and wait (**block**) for slow operations like database calls or API requests.
- **Async** functions can **pause** during waiting and let the server handle other requests in that time.

### Key Words
- `async def` → makes a function async
- `await` → tells Python to wait for something (like sleep or API call) **without blocking** the whole server
- `asyncio` → Python's built-in library for async

## When to Use Async?
Use async for **I/O-bound work**:
- Database queries
- External API calls
- File reading/writing
- Network requests

> **Note:** Do **NOT** use async for CPU-heavy work (like heavy calculations) – use `threads` or `multiprocessing` for that.

## What I Did Today
1. **Made `/sync-slow`**: blocking – bad for many users.
2. **Made `/async-slow`**: with `await asyncio.sleep(2)` – non-blocking.
3. **Made `/external`**: calling real API using `httpx.AsyncClient()`.
4. **Made `/concurrent`**: runs 3 slow tasks together → finishes in ~2 seconds instead of 6.

## Real World Benefit
If **100 users** click at the same time:
- **Sync** → takes 100 × 2 = **200 seconds** (slow!)
- **Async** → all finish in **~2 seconds** (fast!)

## Important Points
- **FastAPI** by default supports async routes.
- Use `await` only inside `async def` functions.
- Use `httpx.AsyncClient()` for async external calls.
- Async makes API handle **thousands of users** smoothly.
