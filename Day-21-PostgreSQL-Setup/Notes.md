**what is a database?**
- an organize collection of data
- a method to store and retrieve data
- a method to manipulate and access the data

*** What is a database vs DBMS**
- Database is the collection of data
- DBMS is the system that manages the database


*** what is RDBMS?**
- Relational Database Management System
- It is a database that stores data in a tabular format
- It uses tables to store data
- a type of database system that store data in structured tables (using rows and columns)
- it uses SQL (structured query language) to manage the database


*** PostgreSQL Setup (Day 21)**
- **Installation:** Local (Homebrew)
- **Port:** 5433
- **Database:** fastapi_db
- **User:** postgres
- **Password:** 1234
- **Connection String:** `postgresql://postgres:1234@localhost:5433/fastapi_db`

**Practice Files:**
- `sql/setup.sql`: Creates database and table.
- `sql/queries.sql`: Contains CRUD practice examples.
- `src/connect_test.py`: Python script to verify connection.
