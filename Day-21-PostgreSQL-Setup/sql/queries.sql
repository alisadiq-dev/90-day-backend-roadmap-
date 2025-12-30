-- 0. INSERT (Create Data)
-- Insert a single user
INSERT INTO users (email, name) 
VALUES ('new.user@example.com', 'New User');

-- Insert multiple users
INSERT INTO users (email, name) VALUES 
('hamza@example.com', 'Hamza Ali'),
('zainab@example.com', 'Zainab Bibi');

-- 1. SELECT (Read Data)
-- Get all users
SELECT * FROM users;

-- Get specific fields
SELECT name, email FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE name = 'Ali Sadiq';

-- Advanced SELECT: Order by name (A-Z)
SELECT * FROM users ORDER BY name ASC;

-- Advanced SELECT: Limit results (Show only first 3)
SELECT * FROM users LIMIT 3;

-- Advanced SELECT: Pattern Matching (Names starting with 'A')
SELECT * FROM users WHERE name LIKE 'A%';

-- 2. UPDATE (Modify Data)
-- Update Ali's email
UPDATE users 
SET email = 'ali.new@example.com' 
WHERE name = 'Ali Sadiq';

-- Verify the update
SELECT * FROM users WHERE name = 'Ali Sadiq';

-- 3. DELETE (Remove Data)
-- Delete user with id 5
DELETE FROM users WHERE id = 5;

-- Verify deletion
SELECT * FROM users;
