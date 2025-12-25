# Day 20: Background Tasks & Middleware in FastAPI

Welcome to Day 20 of the Backend Roadmap! Today, we are exploring two powerful features of FastAPI: **Middleware** and **Background Tasks**. These tools allow you to handle cross-cutting concerns and improve application performance.

---

## 1. Middleware in FastAPI

### What is Middleware?
Middleware is a function that runs **before** every request is processed by a path operation and **after** every response is returned. You can think of it as a "filter" or a "wrapper" around your entire application.

### Why use Middleware?
- **Logging**: Log every request and response.
- **Timing**: Measure how long a request takes to process.
- **Security**: Add security headers or check authentication tokens.
- **CORS**: Handle Cross-Origin Resource Sharing.

### Implementation Example (`src/middleware.py`)

In this project, we implemented two custom middlewares using `BaseHTTPMiddleware`.

#### A. Timing Middleware
This middleware calculates the time taken to process a request and adds it to the response headers.

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()  # 1. Start timer
        
        # 2. Pass the request to the next handler (route or middleware)
        response = await call_next(request)
        
        # 3. Request is finished, calculate time
        process_time = time.time() - start_time
        
        # 4. Add custom header to the response
        response.headers["X-Process-Time"] = str(process_time)
        return response
```

#### B. Custom Header Middleware
This adds a static custom header to every response.

```python
class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Header Value"
        return response
```

---

## 2. Background Tasks in FastAPI

### What are Background Tasks?
Background Tasks allow you to run functions **after** returning a response. This is crucial for tasks that take a long time to complete and shouldn't block the user.

### Why use Background Tasks?
- **Sending Emails**: Sending an email can take 2-5 seconds. You don't want the user to wait for that.
- **Image Processing**: Resizing or processing uploaded images.
- **Heavy Logging**: Saving detailed logs to a database or external service.

### Implementation Example (`src/background.py`)

Here we simulate a slow process like sending an email using `asyncio.sleep`.

```python
import asyncio

async def send_welcome_email(email: str):
    print(f"Sending welcome email to {email}")
    # Simulate a slow network request (5 seconds)
    await asyncio.sleep(5)
    print(f"Welcome email sent to {email}")
```

### Integration in Routes (`src/main.py`)

To use background tasks, simply add a parameter of type `BackgroundTasks` to your route function.

```python
from fastapi import FastAPI, BackgroundTasks
from src.background import send_welcome_email

app = FastAPI()

@app.post("/register")
async def register_user(email: str, background_tasks: BackgroundTasks):
    # This adds the task to the queue to be executed after the response is sent
    background_tasks.add_task(send_welcome_email, email)
    
    # The user gets this response immediately (they don't wait 5 seconds)
    return {"message": "Registration successful! Welcome email on the way"}
```

---

## 3. How the Flow Works

1. **Request Arrives**: The `TimingMiddleware` starts the clock.
2. **Middleware Chain**: The request passes through any other middlewares.
3. **Route Handler**: `register_user` is called. It calculates the response and queues the `send_welcome_email` task.
4. **Response Sent**: FastAPI sends the response back to the user immediately.
5. **After Response**: FastAPI starts executing the queued Background Task (`send_welcome_email`).
6. **Middleware Finish**: The `TimingMiddleware` finishes the clock and adds the header to the response on its way out.

---

## Summary
- **Middleware**: Best for logic that needs to run for *every* request (logging, headers).
- **Background Tasks**: Best for logic that is *triggered* by a request but can run asynchronously (emails, processing).
