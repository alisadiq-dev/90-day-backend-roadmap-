# Day 19 – Dependency Injection in FastAPI

Today I learned **Dependency Injection** – FastAPI ka sabse powerful feature!

### What I Did
- Created reusable dependencies:
  - `get_pagination()` → skip & limit handle karta hai
  - `get_user_or_404()` → user exists check karta hai aur 404 deta hai
- Refactored Day 17 CRUD routes to use these dependencies
- Routes ab bohot clean ho gaye – logic alag file mein move ho gaya

### Features
- Pagination → `/users/?skip=0&limit=5`
- Automatic 404 if user ID not found
- Code repeat nahi – dependencies reuse kar rahe hain
- Cleaner route handlers

### How to Run
```bash
uvicorn src.main:app --reloadn