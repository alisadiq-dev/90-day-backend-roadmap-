 
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base

class User(Base):
    __tablename__ = "users"           

    id = Column(Integer, primary_key=True, index=True)
    # Primary key, auto-increment, indexing for fast lookup

    email = Column(String(255), unique=True, nullable=False, index=True)
    # Unique email, required field, index for fast queries

    name = Column(String(255), nullable=False)
    # User's name, required field

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # Automatic timestamp jab record banega