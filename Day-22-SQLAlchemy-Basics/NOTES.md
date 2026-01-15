# Day 22 Notes: SQLAlchemy ORM Basics

## Key Concepts

### 1. SQLAlchemy ORM
Object Relational Mapping (ORM) allows us to interact with the database using Python classes and objects instead of raw SQL queries. This makes the code more readable, maintainable, and database-agnostic.

### 2. Engine and Session
- **Engine:** The entry point to the database, managing the pool of connections. Created using `create_engine`.
- **Session:** The handle to the database for a specific transaction or unit of work. Created using `sessionmaker`.

### 3. Declarative Base
`declarative_base()` allows us to define classes that map to database tables. Our models inherit from this base class.

### 4. CRUD Operations
- **Create:** Instantiate a model object, `add()` it to the session, and `commit()`.
- **Read:** Use `query()` with methods like `all()`, `first()`, `filter()`, `offset()`, and `limit()`.
- **Update:** Retrieve an object, modify its attributes, and `commit()`.
- **Delete:** Retrieve an object, `delete()` it from the session, and `commit()`.

### 5. Pydantic vs SQLAlchemy
- **SQLAlchemy Models:** Map to database tables. Used for DB interaction.
- **Pydantic Models (Schemas):** Used for data validation and serialization (request/response bodies) in FastAPI (though strictly speaking, this specific Day 22 specific doesn't use Pydantic yet, it is the typical next step).
