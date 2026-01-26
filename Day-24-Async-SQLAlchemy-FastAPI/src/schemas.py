# src/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str | None = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True