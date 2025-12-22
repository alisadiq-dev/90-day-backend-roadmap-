# Day 19: Dependency Injection in FastAPI

## What is Dependency Injection (DI)?

Dependency Injection is a design pattern where an object (or function) receives other objects or "dependencies" that it needs, rather than creating them itself.

In simple terms: **"Don't build it yourself, ask for it."**

In FastAPI, DI is a first-class citizen and is extremely powerful. It allows you to:
1.  **Share logic** (reuse the same code logic in multiple path operations).
2.  **Share database connections**.
3.  **Enforce security**, authentication, and role requirements.
4.  **Minimize code repetition**.

## How FastAPI Handles Dependencies

FastAPI provides a powerful Dependency Injection system. You declare dependencies in your *path operation functions* (your API routes) and FastAPI handles the rest.

### The `Depends` Import

To use dependencies, you import `Depends` from `fastapi`.

```python
from fastapi import Depends
```

## Code Walkthrough

Let's look at how we implemented Dependency Injection for **Pagination** in our project.

### 1. The Dependency Function (`src/dependencies.py`)

This function defines *what* we need. In this case, we need `skip` and `limit` query parameters to handle pagination.

```python
# src/dependencies.py
from fastapi import Query

# This is our dependency function
def get_pagination(
    skip: int = Query(0, ge=0),          # default 0, must be positive
    limit: int = Query(10, ge=1, le=100) # default 10, min 1, max 100
):
    # It returns a dictionary that will be "injected" into our path operation
    return {"skip": skip, "limit": limit}
```

*   **Logic**: It handles the validation of `skip` and `limit`.
*   **Reuse**: We can use `get_pagination` in *any* route that needs pagination, without rewriting these 4 lines of code.

### 2. Injecting the Dependency (`src/main.py`)

Now we use the dependency in our main application.

```python
# src/main.py
from fastapi import FastAPI, Depends
from src.dependencies import get_pagination
from src.crud import get_all_users

app = FastAPI()

# ... users_db ...

@app.get("/users")
def read_users(pagination: dict = Depends(get_pagination)):
    # FastAPI does the following:
    # 1. Calls get_pagination()
    # 2. Gets the result {"skip": ..., "limit": ...}
    # 3. Assigns that result to the 'pagination' argument here
    
    return get_all_users(users_db, pagination)
```

*   **`pagination: dict = Depends(get_pagination)`**: This is the magic line.
    *   It tells FastAPI: "Before running `read_users`, please run `get_pagination`."
    *   "Take whatever `get_pagination` returns, and give it to me in the `pagination` variable."

### 3. Using the Injected Data (`src/crud.py`)

The `read_users` function calls `get_all_users` and passes the injected `pagination` dictionary.

```python
# src/crud.py
def get_all_users(users_db: list, pagination: dict):
    skip = pagination["skip"]
    limit = pagination["limit"]
    
    # Python list slicing to paginate
    return users_db[skip : skip + limit]
```

## Why is this better?

### Without Dependency Injection
If we didn't use DI, `read_users` would look like this:

```python
@app.get("/users")
def read_users(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100)
):
    pagination = {"skip": skip, "limit": limit} # We repeat this logic 
    return get_all_users(users_db, pagination)
```

If you have 10 endpoints that need pagination, you would copy-paste those `skip` and `limit` arguments 10 times. If you wanted to change the default limit from 10 to 20, you'd have to change it in 10 places.

### With Dependency Injection
You change it **once** in `get_pagination` inside `src/dependencies.py`, and it updates everywhere.

## Key Takeaways
1.  **Dependencies** are just functions.
2.  Use **`Depends`** to declare them in your path operations.
3.  FastAPI executes the dependency code before your path operation.
4.  It keeps your code **DRY** (Don't Repeat Yourself) and easier to maintain.
