# Day 21: PostgreSQL Setup

This project demonstrates how to set up and connect to a PostgreSQL database locally using Python.

## Prerequisites

- Python 3.11+
- PostgreSQL (v14 used in this setup)

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
    -   **Port:** 5433 (Configured to avoid conflicts with default 5432)
    -   **User:** `postgres`
    -   **Password:** `1234`
    -   **Database:** `fastapi_db`

4.  **Initialize Database:**
    Run the setup script to create the database and table:
    ```bash
    psql -p 5433 -U postgres -f sql/setup.sql
    ```

## Usage

### Verify Connection
Run the Python script to test the connection and fetch data:
```bash
python src/connect_test.py
```

### Practice CRUD
You can practice CRUD operations using the queries provided in `sql/queries.sql`.

## Project Structure
- `src/`: Python source code.
- `sql/`: SQL scripts for setup and queries.
- `Notes.md`: Learning notes and connection details.
