 # src/crud.py
# Day 17 ka logic yahan move kiya – single source of truth

from typing import List, Dict

users_db = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Ahmed"},
    {"id": 4, "name": "Fatima"},
    {"id": 5, "name": "Usman"},
    {"id": 6, "name": "Dua"},
    {"id": 7, "name": "Adeen"},
    {"id": 8, "name": "Wania"},
    {"id": 9, "name": "Ayesha"},
    {"id": 10, "name": "Hafiza"},
]

def get_all_users(pagination: dict) -> List[Dict]:
    skip = pagination["skip"]
    limit = pagination["limit"]
    return users_db[skip:skip + limit]

def create_user(user_data: dict) -> Dict:
    global users_db
    new_user = user_data.copy()
    new_user["id"] = len(users_db) + 1
    users_db.append(new_user)
    return new_user

def get_user_by_id(user_id: int) -> Dict:
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id: int, update_data: dict) -> Dict:
    for user in users_db:
        if user["id"] == user_id:
            user.update(update_data)
            return user
    return None

def delete_user(user_id: int) -> bool:
    global users_db
    for i, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db.pop(i)
            return True
    return False