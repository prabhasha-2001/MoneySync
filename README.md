# MoneySync | Personal Finance Visualizer & Predictor

MoneySync helps you track, visualize, and plan your personal finances with ease. Get insights, alerts, and interactive charts to manage your money better.

## Features
Dashboard: Real-time balance, interactive spending charts, recent 5 transactions
Transactions: Manual entry, CSV bulk upload, search & filter
Insights: Spending patterns, overspend alerts
Secure Login: Encrypted password authentication

## Tech Stack
Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript (Chart.js)
Backend: Python (Flask)
Database: MySQL
Data Analysis: Pandas
Templating: Jinja2

##  Project Structure
```text
MoneySync/
├── static/          # CSS, JS, images
├── templates/       # HTML templates
├── data_science/    # Python logic for predictions & analysis
├── extensions.py    # Flask + MySQL config
├── auth.py          # Login/Signup routes
├── routes.py        # Main app routes
├── utils.py         # Helper functions
├── schema.sql       # Database structure
└── app.py           # App entry point
```

## Setup
1. Install Python 3.x & MySQL

2. Create database & import schema.sql
SOURCE path/to/schema.sql;

3. Install dependencies
pip install flask flask-mysqldb pandas

4. Update DB credentials in app.py / extensions.py
```text   
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'moneysync_db'
```

6. Run the app
python app.py

Visit http://127.0.0.1:5000 in your browser.




## Clone the repository
git clone https://github.com/prabhasha-2001/MoneySync.git
cd MoneySync 
