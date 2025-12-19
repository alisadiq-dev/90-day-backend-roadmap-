# My Personal Notes - Day 17: CRUD Operations (In-Memory)

Today, on Day 17, I built a full CRUD API - Create, Read, Update, and Delete!

## What is CRUD?

- **Create**: Add a new user (POST)
- **Read**: View users (GET)
- **Update**: Change user details (PUT)
- **Delete**: Remove a user (DELETE)

## What I Did on Day 17

- **In-memory storage**: Saved users in a list (without a real database).
- **POST /users**: Create a new user, auto-assigning ID.
- **GET /users**: Show all users.
- **GET /users/{id}**: Show a specific user; return 404 error if not found.
- **PUT /users/{id}**: Update a user.
- **DELETE /users/{id}**: Delete a user.
- **Proper status codes**: Used 201 for successful creation, 404 for not found errors.
- **Edge case handling**: Managed duplicate emails and attempts to delete non-existent users.

## Benefits

- **Real-world relevance**: Real APIs are 80% CRUD operations.
- **Professionalism**: Using correct status codes makes the API look professional.
- **Stability**: Proper error handling prevents the application from crashing.
- **Testing**: Testing the endpoints in Postman was a great experience.

## Extra Notes

- I can use `HTTPException` to return custom errors with specific status codes.
- Started with a fake DB today; I will add real PostgreSQL tomorrow.
- Pydantic validation is still working effectively (carried over from Day 16).

## Conclusion

Day 17 is complete. My API is now a fully functional CRUD application and behaves like a production system!
Tomorrow I will add a database so data persists even after a restart.
