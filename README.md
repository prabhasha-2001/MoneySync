MoneySync | Personal Finance Visualizer & Predictor
MoneySync is a smart personal finance management web application designed to help users take control of their financial health. By tracking daily transactions, visualizing spending habits through interactive charts, and providing intelligent insights into future expenses, MoneySync simplifies money management for everyone.

Features
1. Smart Dashboard
Real-time Balance: Automatically calculates your total balance by factoring in both income and expenses.

Visual Analytics: View your spending distribution across different categories (Food, Rent, Transport, etc.) using interactive Chart.js doughnut charts.

Recent Activity: A quick-glance table showing your most recent 5 transactions.

2. Transaction Management
Manual Entry: Add transactions easily with categories, descriptions, and dates.

CSV Bulk Upload: Skip manual entry by importing your bank statements directly via CSV files.

Filtered View: Search and filter your entire transaction history by description or category.

3. Intelligent Insights
Smart Guidance: The system analyzes your past spending behavior to identify patterns.

Overspend Warning: Receive alerts if your current habits suggest you might exceed your typical limits next month.

4. Secure Authentication
User registration and login system with encrypted password hashing to keep your financial data private and secure.

Tech Stack
Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript (Chart.js)

Backend: Python (Flask Framework)

Database: MySQL

Data Analysis: Pandas (for CSV processing and spending insights)

Templating: Jinja2

Project Structure
Plaintext
MoneySync/
├── static/                # CSS, JS, and Image assets
├── templates/             # HTML templates (Dashboard, Login, etc.)
├── data_science/          # Python logic for ML predictions and analysis
├── extensions.py          # Flask extensions configuration (MySQL)
├── auth.py                # Authentication routes (Login/Signup)
├── routes.py              # Main application routes (Dashboard, Transactions)
├── utils.py               # Helper functions (Formatting, Validations)
├── schema.sql             # Database structure and seed data
└── app.py                 # Application entry point

Installation & Setup

1. Prerequisites
Python 3.x installed.

MySQL Server installed and running.


2. Database Setup
Run the following command in your MySQL terminal or import the schema.sql file in phpMyAdmin:

SQL
SOURCE path/to/schema.sql;

3. Clone and Install Dependencies
Bash

# Clone the repository
git clone 
cd MoneySync

# Install required libraries
pip install flask flask-mysqldb pandas

4. Configuration
Update your database credentials in app.py or extensions.py:

Python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'moneysync_db'

5. Run the Application
Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000.


CSV Import Format
To ensure a successful bulk upload, your CSV file should follow this structure:
| date | category | amount | description |
| :--- | :--- | :--- | :--- |
| 2026-03-25 | Salary | 30000.00 | Monthly Pay |
| 2026-03-31 | Food & Dining | 500.00 | Dinner |


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

