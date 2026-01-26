# src/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src import models, crud, dependencies, schemas
from src.database import engine

app = FastAPI(title="Day 24 - Async FastAPI + SQLAlchemy")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/users/", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(dependencies.get_async_db)):
    try:
        db_user = await crud.create_user(db, email=user.email, name=user.name)
        return db_user
    except Exception:
        raise HTTPException(400, "Email already exists")

@app.get("/users/", response_model=list[schemas.UserOut])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(dependencies.get_async_db)):
    return await crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
async def read_user(user_id: int, db: AsyncSession = Depends(dependencies.get_async_db)):
    return await crud.get_user(db, user_id=user_id)

@app.put("/users/{user_id}", response_model=schemas.UserOut)
async def update_user(user_id: int, user: schemas.UserUpdate, db: AsyncSession = Depends(dependencies.get_async_db)):
    return await crud.update_user(db, user_id=user_id, name=user.name)

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(dependencies.get_async_db)):
    await crud.delete_user(db, user_id=user_id)
    return {"detail": "User deleted"}