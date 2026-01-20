# src/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src import models, crud, dependencies, schemas
from src.database import engine

# Tables create if not exist (Day 21-22 link)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 23 - FastAPI + SQLAlchemy")

@app.post("/users/", response_model=schemas.User)
def create_user(email: str, name: str, db: Session = Depends(dependencies.get_db)):
    try:
        return crud.create_user(db, email=email, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Email already exists")

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.get_user(db, user_id=user_id)

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, name: str, db: Session = Depends(dependencies.get_db)):
    return crud.update_user(db, user_id=user_id, name=name)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    crud.delete_user(db, user_id=user_id)
    return {"detail": "User deleted"}