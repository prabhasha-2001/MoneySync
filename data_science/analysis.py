import pandas as pd

def get_spending_insights(df):
    """
    Takes a DataFrame of transactions and returns category-wise totals.
    """
    if df.empty:
        return {}
    
    expenses = df[df['type'] == 'expense']
    category_totals = expenses.groupby('category_name')['amount'].sum().to_dict()
    
    return category_totals

def detect_budget_overrun(df, budgets):
    """
    Compares current spending vs set budgets.
    """
    insights = []
    category_totals = get_spending_insights(df)
    
    for category, limit in budgets.items():
        current = category_totals.get(category, 0)
        if current > limit:
            insights.append(f"⚠️ Alert: You exceeded your {category} budget by ${current - limit:.2f}!")
            
    return insights