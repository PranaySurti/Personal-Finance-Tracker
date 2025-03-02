import sqlite3

# Initialize the database and create tables
def init_db():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    # Check if 'user_id' exists in transactions table
    cursor.execute("PRAGMA table_info(transactions);")
    columns = [col[1] for col in cursor.fetchall()]  # Get column names

    if "user_id" not in columns:
        print("⚠️ The 'transactions' table is outdated. Recreating it...")

        # Drop the old table (if exists)
        cursor.execute("DROP TABLE IF EXISTS transactions;")

        # Create transactions table (linked to users)
        cursor.execute("""
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        print("✅ Transactions table updated successfully.")

    conn.commit()
    conn.close()


# Add a new user to the database
def add_user(name):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        print(f"✅ User '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"⚠️ User '{name}' already exists. Try another name.")

    conn.close()


# Get all users from the database
def get_users():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


# Get user ID by name
def get_user_id(name):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None


# Add a transaction linked to a user
def add_transaction(user_id, amount, category):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, category) VALUES (?, ?, ?)",
            (user_id, amount, category),
        )
        conn.commit()
        print(f"✅ Transaction of {amount} added for user ID {user_id} under {category}.")
    except sqlite3.Error as e:
        print(f"⚠️ Database error: {e}")

    conn.close()


# Get transactions for a specific user
def get_transactions(user_id):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions


# Initialize the database when the script runs
init_db()
