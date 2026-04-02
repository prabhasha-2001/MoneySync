from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import mysql
import MySQLdb.cursors

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        cursor = mysql.connection.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)', 
                           (username, email, password))
            mysql.connection.commit()
            flash('Account created! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except:
            flash('Email or Username already exists.', 'danger')
            
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
