import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_month_spending(user_transactions):
    """
    Predicts the total spending for the upcoming month.
    Expects a DataFrame with 'month_index' and 'total_amount'.
    """
    if len(user_transactions) < 3:
        return "Not enough data for AI prediction (Need at least 3 months)."

    X = user_transactions[['month_index']].values
    y = user_transactions['total_amount'].values

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[X[-1][0] + 1]])
    prediction = model.predict(next_month)

    return round(float(prediction[0]), 2)