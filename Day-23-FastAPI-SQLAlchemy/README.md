# Day 23 - FastAPI + SQLAlchemy CRUD API

A complete RESTful API built with **FastAPI** and **SQLAlchemy** for managing users. This project demonstrates how to integrate a PostgreSQL database with FastAPI using SQLAlchemy ORM, implementing full CRUD (Create, Read, Update, Delete) operations.

## Project Structure

```
Day-23-FastAPI-SQLAlchemy/
├── src/
│   ├── __init__.py         # Package initializer
│   ├── main.py             # FastAPI application & route definitions
│   ├── database.py         # Database connection & session configuration
│   ├── models.py           # SQLAlchemy ORM models
│   ├── crud.py             # Database operations (Create, Read, Update, Delete)
│   └── dependencies.py     # FastAPI dependency injection for database sessions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── NOTES.md                # Learning notes and explanations
```

## Tech Stack

| Technology   | Purpose                                    |
|--------------|-------------------------------------------|
| FastAPI      | Modern, fast web framework for building APIs |
| SQLAlchemy   | Python SQL toolkit and ORM                |
| PostgreSQL   | Relational database                       |
| Pydantic     | Data validation (built into FastAPI)      |
| Uvicorn      | ASGI server for running the application   |

## Prerequisites

- Python 3.10+
- PostgreSQL installed and running
- A database named `fastapi_db` created in PostgreSQL

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Day-23-FastAPI-SQLAlchemy
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary uvicorn
   ```

4. **Configure the database**
   
   Update the `DATABASE_URL` in `src/database.py` with your PostgreSQL credentials:
   ```python
   DATABASE_URL = "postgresql://username:password@localhost/fastapi_db"
   ```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn src.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Endpoints

| Method   | Endpoint            | Description           |
|----------|---------------------|-----------------------|
| `POST`   | `/users/`           | Create a new user     |
| `GET`    | `/users/`           | Get all users         |
| `GET`    | `/users/{user_id}`  | Get a specific user   |
| `PUT`    | `/users/{user_id}`  | Update a user's name  |
| `DELETE` | `/users/{user_id}`  | Delete a user         |

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Example Usage

### Create a User
```bash
curl -X POST "http://127.0.0.1:8000/users/?email=john@example.com&name=John"
```

### Get All Users
```bash
curl -X GET "http://127.0.0.1:8000/users/"
```

### Get a User by ID
```bash
curl -X GET "http://127.0.0.1:8000/users/1"
```

### Update a User
```bash
curl -X PUT "http://127.0.0.1:8000/users/1?name=John%20Doe"
```

### Delete a User
```bash
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

## Key Concepts Demonstrated

- **SQLAlchemy ORM**: Object-Relational Mapping for database interactions
- **Dependency Injection**: Using FastAPI's `Depends()` for database session management
- **Session Management**: Proper handling of database sessions with `yield` and `finally`
- **Auto Table Creation**: Tables are automatically created on application startup
- **Error Handling**: HTTP exceptions for user-friendly error responses

## License

This project is part of the 90-Day Backend Roadmap learning journey.
