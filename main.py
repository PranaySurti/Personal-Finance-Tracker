import cli
import gui

def main():
    while True:
        print("\n===================================")
        print("  Personal Finance Tracker 💰📊")
        print("===================================")
        print("1️⃣ Add Transaction")
        print("2️⃣ View Transactions")
        print("3️⃣ Exit")

        choice = input("\nChoose an option (1/2/3): ")

        if choice == "1":
            cli.add_transaction()  # Calls function to add a transaction
        elif choice == "2":
            cli.view_transactions()  # Fetches and displays transactions
        elif choice == "3":
            print("\nExiting... Have a great day! 😊")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
