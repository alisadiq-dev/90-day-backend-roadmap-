# src/crud.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from src.models import User

async def create_user(db: AsyncSession, email: str, name: str) -> User:
    db_user = User(email=email, name=name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(User).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def get_user(db: AsyncSession, user_id: int) -> User:
    result = await db.execute(select(User).filter_by(id=user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def update_user(db: AsyncSession, user_id: int, name: str) -> User:
    user = await get_user(db, user_id)
    user.name = name
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user(db, user_id)
    await db.delete(user)
    await db.commit()