from flask import Flask, request, jsonify
from db_config import app, mysql

@app.route('/employees', methods=['GET'])
def get_all_employees():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    return jsonify(employees)

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    return jsonify(employee) if employee else ("Employee not found", 404)

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO employees (name, email, department, salary) VALUES (%s, %s, %s, %s)",
        (data['name'], data['email'], data['department'], data['salary'])
    )
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Employee added successfully"}), 201

@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE employees SET name=%s, email=%s, department=%s, salary=%s WHERE id=%s",
        (data['name'], data['email'], data['department'], data['salary'], id)
    )
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Employee updated successfully"})

@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Employee deleted successfully"})
