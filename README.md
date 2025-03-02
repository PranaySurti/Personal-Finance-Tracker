# Personal-Finance-Tracker

Here's a **README.md** file for your **Personal Finance Tracker** project:  

```md
# 💰 Personal Finance Tracker  

A **simple yet powerful** Personal Finance Tracker built with **Python** and **Streamlit**, using **SQLite** for database management. This application helps users track their expenses and manage financial transactions effortlessly.

---

## 🚀 Features  
✅ **User Profiles** – Create and manage multiple user profiles  
✅ **Transaction Management** – Add, view, and categorize transactions  
✅ **Data Persistence** – Uses **SQLite** to store user data securely  
✅ **Interactive UI** – Built with **Streamlit** for a seamless experience  
✅ **Expense Categories** – Classify transactions for better insights  

---

## 📌 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```bash
streamlit run gui.py
```

---

## 📊 Database Schema  
### **Users Table**  
| Column | Type | Description |
|--------|------|------------|
| `id` | INTEGER | Primary Key (Auto Increment) |
| `name` | TEXT | Unique username |

### **Transactions Table**  
| Column | Type | Description |
|--------|------|------------|
| `id` | INTEGER | Primary Key (Auto Increment) |
| `user_id` | INTEGER | Foreign Key (References `users.id`) |
| `amount` | REAL | Transaction amount |
| `category` | TEXT | Expense category |
| `date` | TIMESTAMP | Default: Current Timestamp |

---

## 🛠 Technologies Used  
- **Python** – Backend logic  
- **SQLite** – Database for storing transactions  
- **Streamlit** – GUI framework for a user-friendly experience  
- **Git & GitHub** – Version control and collaboration  

---

## 📌 TODO & Future Enhancements  
✅ Add budget tracking feature  
✅ Implement graphical expense reports  
✅ Multi-user support with authentication  

---

## 🤝 Contributing  
Contributions are welcome! Feel free to open issues or submit pull requests.  

1. **Fork the repo**  
2. **Create a feature branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m "Added new feature"`)  
4. **Push to GitHub** (`git push origin feature-name`)  
5. **Create a Pull Request**  

---

## 📜 License  
This project is open-source under the **MIT License**.  

🚀 Happy Coding!  
```

### **How to Use This?**
1. **Create a new README.md file** in your project root.
2. Copy-paste the above content.
3. Modify the **GitHub repo URL** (`YOUR_USERNAME` → your actual GitHub username).
4. Commit the README file:
   ```bash
   git add README.md
   git commit -m "Added project README"
   git push origin main
   ```

✅ **Your GitHub repository will now have a professional README!** 🚀

