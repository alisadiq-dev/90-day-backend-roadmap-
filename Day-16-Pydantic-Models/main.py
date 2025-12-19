from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import UserCreate, UserResponse
from typing import List

app = FastAPI(title="Day 16 - Pydantic User API")

fake_db = []
next_id = 1

@app.post("/users/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global next_id
    user_dict = user.dict()
    user_dict["id"] = next_id
    fake_db.append(user_dict)
    next_id += 1
    
    return UserResponse(**user_dict)

@app.get("/users/", response_model=List[UserResponse])
def get_users():
    return [UserResponse(**u) for u in fake_db]