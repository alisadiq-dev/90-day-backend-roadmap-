# SQLAlchemy Basics - Day 22

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using SQLAlchemy ORM with a PostgreSQL database.

## Project Structure

- `src/main.py`: Entry point of the application, running CRUD examples.
- `src/database.py`: Database connection and session setup.
- `src/models.py`: SQLAlchemy models (User table definition).
- `src/crud.py`: Functions performing CRUD operations.

## Setup

1.  **Create Virtual Environment:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Database Configuration:**
    - Ensure PostgreSQL is running.
    - Create a database named `fastapi_db` (or update `DATABASE_URL` in `src/database.py`).
    - Update the username and password in `src/database.py` if different from `postgres:password`.

## Usage

Run the main script to see CRUD operations in action:

```bash
python src/main.py
```
