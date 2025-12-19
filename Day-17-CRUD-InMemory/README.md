 # Day 17 – Full CRUD API (In-Memory)

Today I built a complete **CRUD API** for users using FastAPI!

### What is CRUD?
- **C**reate → add new user (POST)
- **R**ead → get users (GET)
- **U**pdate → change user data (PUT)
- **D**elete → remove user (DELETE)

### Features
- Create user with validation (email, password rules)
- Get all users
- Get single user by ID
- Update user (partial update allowed)
- Delete user
- Proper status codes (201 Created, 404 Not Found, 400 Bad Request)
- Duplicate email protection

### How to Run
```bash
uvicorn main:app --reload