# src/schemas.py
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy models
