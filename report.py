import sqlite3
import matplotlib.pyplot as plt

def plot_expense_pie_chart():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
    data = cursor.fetchall()
    
    if not data:
        print("No expense data available.")
        return

    categories, amounts = zip(*data)
    
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.show()

if __name__ == "__main__":
    plot_expense_pie_chart()
