 # src/main.py
# Day 22 test – ORM se CRUD

from src.database import SessionLocal, engine
from src.models import Base
from src.crud import create_user, get_users, get_user_by_id, update_user, delete_user

# Table create if not exists (Day 21 se link)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Create
new_user = create_user(db, "test@example.com", "Test User")
print("Created:", new_user.id, new_user.email)

# Read all
users = get_users(db)
print("All users:", len(users))

# Read one
user = get_user_by_id(db, new_user.id)
print("Single user:", user.name)

# Update
updated = update_user(db, new_user.id, "Updated Name")
print("Updated name:", updated.name)

# Delete
delete_user(db, new_user.id)
print("Deleted user")

db.close()