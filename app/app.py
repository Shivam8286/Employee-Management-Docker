
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql',
        user='root',
        password='password',
        database='employee_db'
    )

@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', employees=employees)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", (name, position))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    db = get_db_connection()
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        cursor.execute("UPDATE employees SET name=%s, position=%s WHERE id=%s", (name, position, id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('update.html', employee=employee)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

