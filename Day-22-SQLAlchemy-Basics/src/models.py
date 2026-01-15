# src/models.py
# Day 21 ki users table ko Python class mein map kar rahe hain

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base

class User(Base):
    __tablename__ = "users"  # Day 21 mein bani table ka naam

    id = Column(Integer, primary_key=True, index=True)  # Automatic ID
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)  # ← yeh line add kar
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Automatic time