# python_employee_mgmt_api (Flask + MySQL)

## 📌 Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Installation & Setup](#installation--setup)
6. [Database Configuration](#database-configuration)
7. [API Endpoints](#api-endpoints)
8. [Running the Application](#running-the-application)
9. [Testing the APIs](#testing-the-apis)

---

## 📖 Introduction
This is a **Flask REST API** for managing employees, supporting CRUD operations. It connects to a **MySQL** database to store and manage employee records.

---

## 🚀 Features
- Add new employees
- Get all employees
- Get a specific employee by ID
- Update employee details
- Delete an employee

---

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Database:** MySQL
- **ORM:** Flask-MySQLdb
- **Tools:** Postman (for testing), PyCharm/VS Code

---

## 📁 Project Structure
```
python_employee_management_api/
│── com/
│   ├── app/
│   │   ├── app.py            # Main Flask Application
│   │   ├── db_config.py      # Database Configuration
│   │   ├── routes.py         # API Routes
│   │   ├── models.py         # Database Models
│── README.md                 # Project Documentation
│── requirements.txt          # Dependencies
```

---

## 🔧 Installation & Setup
### 1️⃣ **Install Python & MySQL**
Ensure you have **Python 3.10+** and **MySQL** installed.

### 2️⃣ **Set Up Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install Required Packages**
```bash
pip install -r requirements.txt
```
(If `pip` is not recognized, check the environment setup.)

---

## 🎛 Database Configuration
### 1️⃣ **Create MySQL Database**
Login to MySQL and create a database:
```sql
CREATE DATABASE employee_db;
```

### 2️⃣ **Configure Database in `db_config.py`**
Edit `db_config.py` and update credentials:
```python
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'employee_db'

mysql = MySQL(app)
```

---

## 🔥 API Endpoints
| Method | Endpoint               | Description        |
|--------|------------------------|--------------------|
| POST   | `/employee`            | Add new employee  |
| GET    | `/employees`           | Get all employees |
| GET    | `/employee/<id>`       | Get employee by ID |
| PUT    | `/employee/<id>`       | Update employee   |
| DELETE | `/employee/<id>`       | Delete employee   |

---

## ▶️ Running the Application
```bash
python com/app/app.py
```
(Default Flask server runs on `http://127.0.0.1:5000/`)

---

## 🧪 Testing the APIs
Use **Postman** or `curl` commands:

- **Add Employee:**
```bash
curl -X POST http://127.0.0.1:5000/employee -H "Content-Type: application/json" -d '{"name":"John Doe", "age":30, "department":"HR"}'
```

- **Get All Employees:**
```bash
curl -X GET http://127.0.0.1:5000/employees
```

- **Get Employee by ID:**
```bash
curl -X GET http://127.0.0.1:5000/employee/1
```

- **Update Employee:**
```bash
curl -X PUT http://127.0.0.1:5000/employee/1 -H "Content-Type: application/json" -d '{"age":32, "department":"Finance"}'
```

- **Delete Employee:**
```bash
curl -X DELETE http://127.0.0.1:5000/employee/1
```

---

## 🎯 Conclusion
You have successfully built a **Flask REST API with MySQL** for employee management. You can extend this project by adding authentication, logging, or a frontend!

Happy Coding! 🚀

