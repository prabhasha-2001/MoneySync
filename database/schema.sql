-- create database
CREATE DATABASE IF NOT EXISTS moneysync_db;
USE moneysync_db;

-- users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    base_currency VARCHAR(3) DEFAULT 'Rs.', 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type ENUM('income', 'expense') NOT NULL
);

-- transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'Rs.',
    transaction_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    INDEX (transaction_date),
    INDEX (user_id)
);

-- budgets table: 
CREATE TABLE IF NOT EXISTS budgets (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount_limit DECIMAL(15, 2) NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- --- SAMPLE DATA --- --

-- insert categories 
INSERT INTO categories (name, type) VALUES 
('Salary', 'income'), 
('Freelance', 'income'), 
('Food & Dining', 'expense'), 
('Transport', 'expense'), 
('Rent', 'expense'), 
('Entertainment', 'expense'),
('Another', 'expense'); 

-- insert sample user 
INSERT INTO users (username, email, password_hash) VALUES 
('demo_user', 'demo@example.com', 'scrypt:32768:8:1$vY8v...');

-- insert sample transactions 
INSERT INTO transactions (user_id, category_id, amount, transaction_date, description) VALUES 
(1, 1, 30000.00, '2026-03-25', 'Monthly Salary'),
(1, 3, 1000.00, '2026-03-17', 'Lunch at office'),
(1, 6, 500.00, '2026-03-31', 'Movie night'),
(1, 3, 200.00, '2026-03-31', 'Evening tea'),
(1, 5, 12000.00, '2026-03-05', 'Monthly Rent');