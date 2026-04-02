from flask import Blueprint, render_template, session, redirect, url_for, request
import pandas as pd
from data_science.model import predict_next_month_spending
from data_science.analysis import get_spending_insights  
from extensions import mysql
import MySQLdb.cursors

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    user_id = session['user_id']
    
    cursor.execute("""
        SELECT t.*, c.name as category_name, c.type 
        FROM transactions t 
        JOIN categories c ON t.category_id = c.category_id 
        WHERE t.user_id = %s 
        ORDER BY t.transaction_date DESC LIMIT 5
    """, (user_id,))
    recent_transactions = cursor.fetchall()

    cursor.execute("""
        SELECT 
            SUM(CASE WHEN c.type = 'income' THEN t.amount ELSE -t.amount END) as total 
        FROM transactions t
        JOIN categories c ON t.category_id = c.category_id
        WHERE t.user_id = %s
    """, (user_id,))
    res = cursor.fetchone()
    total_balance = res['total'] if res['total'] is not None else 0.0

    cursor.execute("""
        SELECT t.amount, c.name as category_name, c.type 
        FROM transactions t 
        JOIN categories c ON t.category_id = c.category_id 
        WHERE t.user_id = %s
    """, (user_id,))
    all_transactions = cursor.fetchall()
    
    chart_labels = []
    chart_values = []
    
    if all_transactions:
        df = pd.DataFrame(all_transactions)
        category_totals = get_spending_insights(df)
        chart_labels = list(category_totals.keys())
        chart_values = list(category_totals.values())

    return render_template('dashboard.html', 
                           transactions=recent_transactions, 
                           total_balance=total_balance,
                           chart_labels=chart_labels, 
                           chart_values=chart_values)

@routes_bp.route('/transactions')
def transactions():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    
    search_desc = request.args.get('search', '')
    category_id = request.args.get('category', '')
    
    query = """
        SELECT t.*, c.name as category_name, c.type 
        FROM transactions t 
        JOIN categories c ON t.category_id = c.category_id 
        WHERE t.user_id = %s
    """
    params = [session['user_id']]
    
    if search_desc:
        query += " AND t.description LIKE %s"
        params.append(f"%{search_desc}%")
        
    if category_id:
        query += " AND t.category_id = %s"
        params.append(category_id)
        
    query += " ORDER BY t.transaction_date DESC"
    
    cursor.execute(query, tuple(params))
    transactions = cursor.fetchall()
    
    return render_template('transactions.html', 
                           transactions=transactions, 
                           categories=categories,
                           search_val=search_desc,
                           selected_cat=category_id)

@routes_bp.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        category_id = request.form['category_id']
        amount = request.form['amount']
        description = request.form['description']
        date = request.form['date']
        user_id = session['user_id']
        
        cursor.execute("""
            INSERT INTO transactions (user_id, category_id, amount, description, transaction_date) 
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, category_id, amount, description, date))
        
        mysql.connection.commit()
        return redirect(url_for('routes.dashboard'))

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    return render_template('add_transaction.html', categories=categories)

@routes_bp.route('/predictions')
def predictions():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    cursor = mysql.connection.cursor()
    query = """
        SELECT MONTH(transaction_date) as month_index, SUM(amount) as total_amount 
        FROM transactions 
        WHERE user_id = %s AND category_id IN (SELECT category_id FROM categories WHERE type='expense')
        GROUP BY MONTH(transaction_date)
        ORDER BY month_index ASC
    """
    cursor.execute(query, (session['user_id'],))
    data = cursor.fetchall()
    
    if not data:
        return render_template('predictions.html', prediction=0, error_message="No transactions found.")

    df = pd.DataFrame(list(data), columns=['month_index', 'total_amount'])
    predicted_val = predict_next_month_spending(df)
    
    try:
        final_prediction = round(float(predicted_val), 2)
        error_msg = None
    except (ValueError, TypeError):
        final_prediction = 0
        error_msg = predicted_val 

    return render_template('predictions.html', prediction=final_prediction, error_message=error_msg)