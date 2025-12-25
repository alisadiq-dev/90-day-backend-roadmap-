from fastapi import FastAPI, BackgroundTasks
from src.background import send_welcome_email
from src.middleware import CustomHeaderMiddleware, TimingMiddleware 

app = FastAPI(title = "Day 20 - Background Middleware")

app.add_middleware(CustomHeaderMiddleware)
app.add_middleware(TimingMiddleware)

@app.post("/register")
async def register_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_welcome_email, email)
    return {"message": "Registration successful! Welcome email on the way"}
