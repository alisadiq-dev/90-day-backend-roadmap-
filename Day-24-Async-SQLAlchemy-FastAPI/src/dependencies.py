# src/dependencies.py
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import AsyncSessionLocal

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session