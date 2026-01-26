# Technical Notes - Async FastAPI + SQLAlchemy

##  Core Concepts

### 1. Asynchronous Programming with FastAPI

**Why Async?**
- Non-blocking I/O operations allow handling multiple requests concurrently
- Better performance for I/O-bound operations (database queries, API calls)
- More efficient resource utilization

**Key Async Components:**
```python
async def create_user(db: AsyncSession = Depends(get_async_db)):
    # async/await syntax for non-blocking operations
    db_user = await crud.create_user(db, email=user.email, name=user.name)
    return db_user
```

### 2. SQLAlchemy Async Engine

**Database Configuration (`database.py`):**
```python
# Async engine for PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
```

**Key Points:**
- `postgresql+asyncpg://` - Uses asyncpg driver for async PostgreSQL
- `echo=True` - Logs all SQL queries (useful for debugging)
- `expire_on_commit=False` - Prevents objects from expiring after commit

### 3. Database Session Management

**Dependency Injection Pattern (`dependencies.py`):**
```python
async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
```

**Benefits:**
- Automatic session lifecycle management
- Ensures sessions are properly closed
- Clean separation of concerns
- Easy to test and mock

### 4. ORM Models vs Pydantic Schemas

**SQLAlchemy Model (`models.py`):**
- Represents database table structure
- Handles database operations
- Uses SQLAlchemy Column types

**Pydantic Schema (`schemas.py`):**
- Validates request/response data
- Provides automatic serialization
- Type checking and documentation

**Example Flow:**
```
Request JSON → Pydantic Schema (validation) → SQLAlchemy Model (DB) → Pydantic Schema (response)
```

### 5. CRUD Operations Pattern

**Separation of Concerns:**
- `crud.py` - Pure database logic
- `main.py` - HTTP routing and business logic
- `dependencies.py` - Resource management

**Async CRUD Example:**
```python
async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(User).offset(skip).limit(limit)
    )
    return result.scalars().all()
```

**Key Methods:**
- `db.execute()` - Executes query asynchronously
- `result.scalars()` - Extracts scalar values
- `.all()` - Returns all results as list

### 6. Database Initialization

**Async Table Creation:**
```python
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
```

**Why `run_sync()`?**
- `create_all()` is a synchronous method
- `run_sync()` allows running sync code in async context
- Only runs once at application startup

### 7. Error Handling

**HTTPException for API Errors:**
```python
if user is None:
    raise HTTPException(status_code=404, detail="User not found")
```

**Try-Except for Database Errors:**
```python
try:
    db_user = await crud.create_user(db, email=user.email, name=user.name)
except Exception:
    raise HTTPException(400, "Email already exists")
```

### 8. Email Validation

**Pydantic EmailStr:**
```python
from pydantic import EmailStr

class UserBase(BaseModel):
    email: EmailStr  # Automatic email validation
    name: str
```

### 9. Timestamps

**Automatic Timestamp Creation:**
```python
created_at = Column(
    DateTime(timezone=True), 
    server_default=func.now(), 
    nullable=False
)
```

**Benefits:**
- `server_default=func.now()` - Database sets timestamp
- `timezone=True` - Stores timezone-aware datetime
- Automatic tracking of record creation

### 10. Response Models

**Type-Safe Responses:**
```python
@app.get("/users/", response_model=list[schemas.UserOut])
async def read_users(...):
    return await crud.get_users(db, skip=skip, limit=limit)
```

**Advantages:**
- Automatic serialization
- Response validation
- Auto-generated documentation
- Prevents data leakage (only returns specified fields)

## 🔍 Best Practices Implemented

1. **Async All the Way**: Consistent async/await usage throughout
2. **Dependency Injection**: Clean session management
3. **Type Hints**: Full type annotations for better IDE support
4. **Separation of Concerns**: Clear module responsibilities
5. **Error Handling**: Proper HTTP status codes and error messages
6. **Validation**: Pydantic schemas for data validation
7. **Documentation**: Auto-generated API docs via FastAPI

## 🚀 Performance Considerations

- **Connection Pooling**: AsyncSessionLocal manages connection pool
- **Non-blocking I/O**: Multiple requests handled concurrently
- **Efficient Queries**: Pagination support (skip/limit)
- **Index Usage**: Email and ID fields indexed for fast lookups

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Async Documentation](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [asyncpg Documentation](https://magicstack.github.io/asyncpg/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
