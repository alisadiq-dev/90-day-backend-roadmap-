from fastapi import FastAPI, HTTPException, status
from models import UserCreate, UserUpdate, UserResponse
from typing import List

app = FastAPI(title = "Day 17 - CRUD User API")

# fake database
users_db = []
next_id = 1

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global next_id
    
    # for duplicate email
    for u in users_db:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    user_dict = user.dict()
    user_dict["id"] = next_id
    users_db.append(user_dict)
    next_id += 1
    
    return UserResponse(**user_dict)

@app.get("/users/", response_model=List[UserResponse])
def get_all_users():
    return [UserResponse(**u) for u in users_db]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for u in users_db:
        if u["id"] == user_id:
            return UserResponse(**u)
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate):
    for u in users_db:
        if u["id"] == user_id:
            update_data = user_update.dict(exclude_unset=True)
            u.update(update_data)
            return UserResponse(**u)
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    global users_db
    for i, u in enumerate(users_db):
        if u["id"] == user_id:
            users_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="User not found")