from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Change as per your MySQL setup
app.config['MYSQL_PASSWORD'] = 'Harshuj7@'  # Change this
app.config['MYSQL_DB'] = 'employee_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
