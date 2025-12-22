 # src/main.py
from fastapi import FastAPI, Depends, HTTPException
from src.dependencies import get_pagination, get_user_or_404
from src.crud import get_all_users, create_user, update_user, delete_user

app = FastAPI(title="Day 19 - DI API")

@app.get("/users")
def read_users(pagination: dict = Depends(get_pagination)):
    return get_all_users(pagination)

@app.get("/users/{user_id}")
def read_user(user = Depends(get_user_or_404)):
    return user

@app.put("/users/{user_id}")
def update_user_route(user_id: int, update_data: dict, user = Depends(get_user_or_404)):
    updated = update_user(user_id, update_data)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user_route(user_id: int, user = Depends(get_user_or_404)):
    if delete_user(user_id):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", status_code=201)
def create_new_user(user_data: dict):
    return create_user(user_data)