from flask import Flask, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from backend.auth import auth_bp
from backend.routes import routes_bp

app = Flask(__name__)

# Configuration 
app.secret_key = 'your_super_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'moneysync_db'

# connect to database
mysql = MySQL(app)

# blueprints 
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(routes_bp)

# Home Page
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('routes.dashboard'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)