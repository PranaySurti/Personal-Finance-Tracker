import sqlite3
import database

def select_user():
    """Allows the user to select or create a profile."""
    users = database.get_users()
    
    if not users:
        print("\n⚠️ No users found. Create a new profile.")
        return create_user()

    print("\n👤 Select a profile:")
    for index, user in enumerate(users, start=1):
        print(f"{index}. {user[1]}")

    print(f"{len(users) + 1}. ➕ Create New User")

    try:
        choice = int(input("Choose an option: "))
        if 1 <= choice <= len(users):
            return users[choice - 1][0]  # Return selected user's ID
        elif choice == len(users) + 1:
            return create_user()
        else:
            print("\n⚠️ Invalid selection. Try again.")
            return select_user()
    except ValueError:
        print("\n⚠️ Please enter a valid number.")
        return select_user()

def create_user():
    """Creates a new user profile."""
    name = input("\nEnter your name: ").strip()
    if not name:
        print("\n⚠️ Name cannot be empty.")
        return create_user()
    
    database.add_user(name)
    return database.get_user_id(name)

def add_transaction(user_id):
    """Prompts user for a transaction and adds it to the database."""
    try:
        amount = float(input("\nEnter transaction amount: "))
        category = input("Enter category (e.g., Food, Transport, Shopping, Others): ").strip()
        if not category:
            print("\n⚠️ Category cannot be empty.")
            return

        database.add_transaction(user_id, amount, category)
        print(f"\n✅ Transaction of ₹{amount} added under {category}!\n")
    except ValueError:
        print("\n⚠️ Invalid input! Please enter a valid amount.")

def view_transactions(user_id):
    """Fetches and displays transactions for the selected user."""
    transactions = database.get_transactions(user_id)

    if not transactions:
        print("\n⚠️ No transactions found.")
    else:
        print("\n=== Transaction History ===")
        for row in transactions:
            print(f"🆔 ID: {row[0]}, 💰 Amount: ₹{row[2]}, 📂 Category: {row[3]}, 📅 Date: {row[4]}")

def cli_menu():
    """CLI menu for the finance tracker with user profiles."""
    print("\n📊 Welcome to Personal Finance Tracker")

    user_id = select_user()  # User selects or creates a profile

    while True:
        print(f"\n👤 Logged in as: {database.get_users()[user_id - 1][1]}")
        print("1️⃣ Add Transaction")
        print("2️⃣ View Transactions")
        print("3️⃣ Switch User")
        print("4️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(user_id)
        elif choice == "2":
            view_transactions(user_id)
        elif choice == "3":
            user_id = select_user()  # Switch user
        elif choice == "4":
            print("\n👋 Exiting... Thank you for using the finance tracker!")
            break
        else:
            print("\n⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    cli_menu()
