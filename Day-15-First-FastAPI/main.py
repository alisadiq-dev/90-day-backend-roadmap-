from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App - Day 15")

# 1. Root route
@app.get("/")
def home():
    return {"message": "Hello World! Welcome to FastAPI"}

# 2. Path parameter  
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "message": f"You asked for item number {item_id}"}

# 3. Query parameter  
@app.get("/search")
def search(q: str | None = None):
    if q:
        return {"search_query": q, "results": f"Searching for: {q}"}
    return {"message": "Please add ?q=something in URL to search"}

@app.get("/about")
def about():
    return {"app": "My Todo API (coming soon)", "day": "Day 15", "status": "Learning FastAPI"}