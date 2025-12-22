# Day 19 – Dependency Injection in FastAPI

Today I learned **Dependency Injection** – FastAPI ka sabse powerful feature!

### What I Did
- Created reusable dependencies:
  - Pagination (`skip` & `limit`)
  - User exists validation (404 if not found)
- Refactored Day 17 CRUD routes to use these dependencies
- Routes ab bohot clean ho gaye – logic alag file mein move ho gaya

### Features
- Pagination → `/users/?skip=0&limit=5`
- Automatic 404 if user ID not found
- Code repeat nahi – dependencies reuse kar rahe hain
- Cleaner route handlers

### How to Run
```bash
uvicorn src.main:app --reload