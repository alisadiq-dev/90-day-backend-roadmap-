# My Personal Notes - Day 16: Pydantic 2.0 Models

> **Summary:** Today I fully understood the concept of **Pydantic** – it was great! 🚀 This library ensures data safety in APIs. FastAPI uses it to prevent invalid data from entering and provides automatic error messages.

---

##  What is Pydantic?

**Pydantic** is a Python library that **checks and validates data**. You create models, and it automatically verifies whether the data is correct or not.

> *Analogy:* Just like a form warns you "invalid email" while filling it out, Pydantic does the exact same job on the backend.

---

##  Why Use It?

1.  **Automatic Validation** 
    *   Triggers an error if invalid data is received.
2.  **Security (Request vs Response)** 🔒
    *   Separate models for Input and Output (e.g., hiding passwords in response).
3.  **Type Coercion** 🔄
    *   Automatically converts types (e.g., if a number comes as a string `"25"`, it converts it to `int` `25`).
4.  **Field Validators** 🛠️
    *   Apply custom rules (e.g., password min 8 chars, email format check).
5.  **FastAPI Integration** ⚡
    *   FastAPI and Pydantic are the best pair – making APIs fast and secure.

---

##  Files and Their Purpose

| File Name | Purpose |
| :--- | :--- |
| **`models.py`** | pydantic models are created here, such as `UserCreate` (input) and `UserResponse` (output). This defines what data the API should accept and what it should return. |
| **`main.py`** | Contains FastAPI routes that use these Pydantic models. These are the actual API endpoints tested via Postman. |

---

## \ Full Concept Step by Step

### 1. Create `UserCreate` Model (Input)
*   **Email:** Use `EmailStr` (automatic valid email check).
*   **Password:** Set `min_length=8`.
*   **Age:** Set `gt=0` (greater than 0).
*   **Custom Validator:** Can be added (e.g., password must contain a number).

### 2. Create `UserResponse` Model (Output)
*   It should return `id`, `email`, `age` but **not the password** (for security).
*   **Config:** Add `class Config: from_attributes = True` to enable direct conversion from database models.

### 3. Create POST `/users` Route
*   Accepts `UserCreate` model.
*   Validates & saves data.
*   Returns `UserResponse`.

### 4. Test in Postman
*   **Valid Data:** `201 Created` success. 🎉
*   **Invalid Data:** `422 Unprocessable Entity` with a message (e.g., "password too short"). ❌

---

## What are the Benefits?

*    **Automatic validation** – invalid data will not enter the API.
*    **Clear error messages** – the user will know exactly what is wrong.
*    **Separate request/response** – ensures security + clean API.
*    **FastAPI Core** – real production APIs are built this way.

---

##  Important Notes

> [!TIP]
> **Pydantic 2.0 Tips:**
> *   Use `Field` – you can put `min_length`, `gt`, etc., inside it.
> *   Use `@validator` for custom checks (e.g., password must have a capital letter).
> *   FastAPI automatically converts Pydantic models to **JSON**.
