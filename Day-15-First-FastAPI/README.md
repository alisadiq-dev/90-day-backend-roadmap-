# Day 15 – My First FastAPI App

Today I made my first working FastAPI server!

### What I Did
- Installed FastAPI and Uvicorn
- Created 4 routes:
  - GET / → Hello World
  - GET /items/{item_id} → path parameter
  - GET /search?q=... → query parameter
  - Auto docs at /docs

### How to Run
```bash
uvicorn main:app --reload