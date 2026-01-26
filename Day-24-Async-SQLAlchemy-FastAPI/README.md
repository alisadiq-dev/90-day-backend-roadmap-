# Day 24 - Async FastAPI + SQLAlchemy

A modern, asynchronous REST API built with FastAPI and SQLAlchemy demonstrating async database operations with PostgreSQL.

##  Features

- **Async/Await**: Full async support using `asyncpg` and SQLAlchemy async engine
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality for users
- **Auto Documentation**: Interactive API docs at `/docs` (Swagger UI)
- **Type Safety**: Pydantic schemas for request/response validation
- **Database**: PostgreSQL with async connection pooling

##  Prerequisites

- Python 3.11+
- PostgreSQL database running locally
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone and navigate to the project**:
   ```bash
   cd Day-24-Async-SQLAlchemy-FastAPI
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**:
   - Update `DATABASE_URL` in `src/database.py` with your PostgreSQL credentials:
   ```python
   DATABASE_URL = "postgresql+asyncpg://username:password@localhost/database_name"
   ```

## 🏃 Running the Application

Start the development server:
```bash
uvicorn src.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

##  API Endpoints

### Create User
```bash
POST /users/
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "John Doe"
}
```

### Get All Users
```bash
GET /users/?skip=0&limit=100
```

### Get Single User
```bash
GET /users/{user_id}
```

### Update User
```bash
PUT /users/{user_id}
Content-Type: application/json

{
  "name": "Jane Doe"
}
```

### Delete User
```bash
DELETE /users/{user_id}
```

##  Project Structure

```
Day-24-Async-SQLAlchemy-FastAPI/
├── src/
│   ├── __init__.py          # Package marker
│   ├── main.py              # FastAPI app & routes
│   ├── database.py          # Async engine & session config
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic validation schemas
│   ├── crud.py              # Database operations
│   └── dependencies.py      # Dependency injection (DB session)
├── venv/                    # Virtual environment
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── NOTES.md                # Technical notes & concepts
```

## 🧪 Testing with cURL

```bash
# Create a user
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "name": "Test User"}'

# Get all users
curl "http://127.0.0.1:8000/users/"

# Get specific user
curl "http://127.0.0.1:8000/users/1"

# Update user
curl -X PUT "http://127.0.0.1:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'

# Delete user
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

##  Interactive Documentation

Visit `http://127.0.0.1:8000/docs` for Swagger UI interactive documentation where you can test all endpoints directly in your browser.

## 🔑 Key Technologies

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM with async support
- **asyncpg**: Fast PostgreSQL database client library
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: Lightning-fast ASGI server

##  License

This is a learning project for the 90-Day Backend Roadmap.
