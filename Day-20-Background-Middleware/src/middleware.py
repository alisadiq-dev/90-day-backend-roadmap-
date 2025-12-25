from fastapi import Request 
from starlette.middleware.base import BaseHTTPMiddleware
import time


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        print(f"MIDDLEWARE: Request started at: {request.method} {request.url}")
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"MIDDLEWARE: Request completed in {process_time:.2f} seconds")
        response.headers["X-Process-Time"] = str(process_time)
        return response


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Header Value"
        return response

        