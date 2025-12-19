from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(gt=0)
    full_name: Optional[str] = None

    @field_validator('password')
    @classmethod
    def strong_password(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError('password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('password must contain at least one digit')
        return v
        
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int
    full_name: Optional[str] = None

    class Config:
        from_attributes = True


    
