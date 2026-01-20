# src/crud.py
from sqlalchemy.orm import Session
from src.models import User
from fastapi import HTTPException

def create_user(db: Session, email: str, name: str) -> User:
    db_user = User(email=email, name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db: Session, user_id: int, name: str) -> User:
    user = get_user(db, user_id)
    user.name = name
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()