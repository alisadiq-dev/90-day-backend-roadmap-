# Day 16 – Pydantic 2.0 Models & Validation

Today I made my API **super safe** with Pydantic!

### What I Did
- UserCreate model with validation:
  - Valid email
  - Password min 8 chars + capital + number
  - Age > 0
- UserResponse → password hide kiya
- POST /users → automatic validation + errors

### Run
```bash
uvicorn main:app --reload