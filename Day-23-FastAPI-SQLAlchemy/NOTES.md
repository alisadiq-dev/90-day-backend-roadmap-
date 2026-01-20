# Day 23 - FastAPI + SQLAlchemy: Complete Learning Notes

## Overview

This project demonstrates how to build a production-ready REST API by integrating **FastAPI** with **SQLAlchemy ORM** and a **PostgreSQL** database. The focus is on implementing CRUD operations with proper database session management and dependency injection.

---

## File-by-File Explanation

### 1. database.py - Database Configuration

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1234@localhost/fastapi_db"   

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

**What Each Line Does:**

| Component         | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `create_engine`   | Creates a connection pool to the PostgreSQL database                   |
| `DATABASE_URL`    | Connection string format: `protocol://user:password@host/database`     |
| `SessionLocal`    | Factory for creating database sessions                                 |
| `autocommit=False`| Transactions are not auto-committed; you must call `commit()` manually |
| `autoflush=False` | Changes are not auto-flushed to DB; provides more control              |
| `declarative_base`| Base class for all ORM models to inherit from                          |

---

### 2. models.py - SQLAlchemy ORM Model

```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

**Column Definitions Explained:**

| Column       | Type          | Constraints                              |
|--------------|---------------|------------------------------------------|
| `id`         | Integer       | Primary key, indexed for fast lookups    |
| `email`      | String(255)   | Unique constraint, cannot be null        |
| `name`       | String(255)   | Cannot be null                           |
| `created_at` | DateTime      | Auto-set to current time on record creation |

**Key Concepts:**

- `__tablename__`: Maps this class to the `users` table in the database
- `primary_key=True`: Marks this column as the unique identifier
- `index=True`: Creates a database index for faster queries
- `unique=True`: Ensures no duplicate values
- `server_default=func.now()`: Database sets the timestamp automatically

---

### 3. dependencies.py - Database Session Dependency

```python
from sqlalchemy.orm import Session
from src.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**How It Works:**

1. `SessionLocal()` creates a new database session
2. `yield db` provides the session to the route handler
3. `finally: db.close()` ensures the session is always closed, even if an error occurs

**Why Use Yield (Generator Function)?**

- The code before `yield` runs **before** the request
- The code after `yield` runs **after** the request completes
- This pattern is called a **context manager** or **dependency with cleanup**

**Lifecycle Diagram:**

```
Request Comes In
       │
       ▼
   db = SessionLocal()   ← Session Created
       │
       ▼
   yield db              ← Session Used by Route
       │
       ▼
   db.close()            ← Session Cleaned Up
```

---

### 4. crud.py - Database Operations

```python
from sqlalchemy.orm import Session
from src.models import User
from fastapi import HTTPException

def create_user(db: Session, email: str, name: str) -> User:
    db_user = User(email=email, name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

**CRUD Operations Breakdown:**

#### CREATE - Adding a New User
```python
db.add(db_user)      # Stage the object for insertion
db.commit()          # Execute the INSERT statement
db.refresh(db_user)  # Reload the object with DB-generated values (like id)
```

#### READ - Fetching Users
```python
# Get all users with pagination
db.query(User).offset(skip).limit(limit).all()

# Get single user by ID
db.query(User).filter(User.id == user_id).first()
```

#### UPDATE - Modifying a User
```python
user.name = name     # Modify the object
db.commit()          # Save changes to database
db.refresh(user)     # Get updated values
```

#### DELETE - Removing a User
```python
db.delete(user)      # Mark for deletion
db.commit()          # Execute the DELETE statement
```

**Error Handling Pattern:**

```python
def get_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

---

### 5. main.py - FastAPI Application

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src import models, crud, dependencies
from src.database import engine

# Tables create if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Day 23 - FastAPI + SQLAlchemy")
```

**Table Auto-Creation:**

```python
models.Base.metadata.create_all(bind=engine)
```

This line:
- Scans all classes that inherit from `Base`
- Creates corresponding tables in the database if they do not exist
- Does NOT modify existing tables (use Alembic for migrations)

**Route with Dependency Injection:**

```python
@app.post("/users/", response_model=models.User)
def create_user(email: str, name: str, db: Session = Depends(dependencies.get_db)):
    try:
        return crud.create_user(db, email=email, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Email already exists")
```

**What Happens Here:**

1. `Depends(dependencies.get_db)` - FastAPI calls `get_db()` automatically
2. The yielded session is passed as `db` parameter
3. After the function returns, the session is closed

---

## Dependency Injection Flow

```
                    ┌─────────────────────────────────────────────┐
                    │              FastAPI Route                  │
                    │  @app.post("/users/")                       │
                    │  def create_user(..., db: Session = Depends(get_db))
                    └───────────────────────────────────────────┬─┘
                                       │
                                       ▼
          ┌─────────────────────────────────────────────────────┐
          │  Dependency: get_db()                               │
          │                                                     │
          │    db = SessionLocal()  ← Create Session            │
          │    yield db             ← Inject into Route         │
          │    db.close()           ← Cleanup After Request     │
          └─────────────────────────────────────────────────────┘
```

---

## Key SQLAlchemy Concepts

### Session Lifecycle

| Stage          | Method        | Description                              |
|----------------|---------------|------------------------------------------|
| Create         | `Session()`   | Opens a connection from the pool         |
| Add            | `add()`       | Stages an object for insertion           |
| Commit         | `commit()`    | Persists all staged changes              |
| Refresh        | `refresh()`   | Reloads object with DB-generated data    |
| Rollback       | `rollback()`  | Undoes all uncommitted changes           |
| Close          | `close()`     | Returns connection to the pool           |

### Query Methods

| Method                     | Purpose                                    |
|----------------------------|--------------------------------------------|
| `query(Model)`             | Start a query on a model                  |
| `.filter(condition)`       | Add WHERE clause                          |
| `.first()`                 | Get first result or None                  |
| `.all()`                   | Get all results as list                   |
| `.offset(n)`               | Skip first n results                      |
| `.limit(n)`                | Limit to n results                        |

---

## Common Patterns and Best Practices

### 1. Always Handle Session Cleanup

```python
# Good - Using try/finally
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 2. Validate Before Database Operations

```python
# Check if user exists before updating
user = get_user(db, user_id)  # Raises 404 if not found
user.name = new_name
```

### 3. Use Response Models

```python
@app.get("/users/", response_model=list[models.User])
```

This tells FastAPI to:
- Validate the response data
- Generate accurate API documentation
- Serialize the data properly

---

## Summary

| File             | Responsibility                            |
|------------------|-------------------------------------------|
| `database.py`    | Database connection and session factory   |
| `models.py`      | ORM model definitions (table structure)   |
| `crud.py`        | All database operations                   |
| `dependencies.py`| Session management via dependency injection |
| `main.py`        | API routes and application setup          |

This separation of concerns makes the code:
- **Maintainable**: Each file has a single responsibility
- **Testable**: CRUD operations can be tested independently
- **Scalable**: Easy to add new models and routes
