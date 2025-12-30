CREATE DATABASE fastapi_db;

\c fastapi_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (email, name) VALUES
('ali@example.com', 'Ali Sadiq'),
('sara@example.com', 'Sara Khan'),
('ahmed@example.com', 'Ahmed Raza'),
('fatima@example.com', 'Fatima Zahra'),
('usman@example.com', 'Usman Malik');