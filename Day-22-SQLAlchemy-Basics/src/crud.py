# src/crud.py
# Python code se CRUD – raw SQL nahi

from sqlalchemy.orm import Session
from src.models import User
from typing import List

def create_user(db: Session, email: str, name: str) -> User:
    db_user = User(email=email, name=name)  # New User object banao
    db.add(db_user)                         # Database mein add karo
    db.commit()                             # Save karo
    db.refresh(db_user)                     # Latest data le aao
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()  # Pagination ke saath sab users

# src/crud.py – get_user_by_id fix
def get_user_by_id(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    return user

def update_user(db: Session, user_id: int, name: str) -> User:
    user = get_user_by_id(db, user_id)
    if user:
        user.name = name
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()