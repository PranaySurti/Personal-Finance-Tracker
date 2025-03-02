import streamlit as st
import sqlite3
import database

# Session state for storing selected user
if "user_id" not in st.session_state:
    st.session_state.user_id = None

def select_user():
    """Allows user to select an existing profile or create a new one."""
    users = database.get_users()
    user_names = [user[1] for user in users]

    st.sidebar.write("### 👤 Select or Create Profile")

    if users:
        selected_user = st.sidebar.selectbox("Choose a profile:", user_names, key="user_selection")
        if selected_user:
            st.session_state.user_id = database.get_user_id(selected_user)

    new_user = st.sidebar.text_input("Enter a new profile name:")

    if st.sidebar.button("➕ Create New Profile"):
        if new_user:
            database.add_user(new_user)
            st.session_state.user_id = database.get_user_id(new_user)
            st.rerun()  # 🔄 Force Streamlit to refresh and update UI
        else:
            st.warning("⚠️ Please enter a name before creating a profile.")


def add_transaction():
    """Allows users to add a transaction linked to their profile."""
    st.subheader("➕ Add Transaction")

    amount = st.number_input("Enter amount:", min_value=0.0, step=0.01)
    category = st.selectbox("Select category:", ["Food", "Transport", "Shopping", "Others"])

    if st.button("Add Transaction"):
        if st.session_state.user_id:
            database.add_transaction(st.session_state.user_id, amount, category)
            st.success(f"✅ Added ₹{amount} to {category}!")
            st.rerun()
        else:
            st.error("⚠️ Please select a profile first.")

def view_transactions():
    """Displays the transaction history for the selected user."""
    st.subheader("📜 Transaction History")

    if st.session_state.user_id:
        transactions = database.get_transactions(st.session_state.user_id)

        if transactions:
            st.table(transactions)
        else:
            st.info("⚠️ No transactions found.")
    else:
        st.error("⚠️ Please select a profile first.")

def run_gui():
    """Main GUI function for the finance tracker."""
    st.title("💰 Personal Finance Tracker")

    select_user()  # User selection in sidebar

    if st.session_state.user_id:
        menu = ["Add Transaction", "View Transactions"]
        choice = st.sidebar.radio("Menu", menu)

        if choice == "Add Transaction":
            add_transaction()
        elif choice == "View Transactions":
            view_transactions()
    else:
        st.warning("⚠️ Please select a profile to continue.")

if __name__ == "__main__":
    run_gui()
