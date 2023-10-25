from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Replace the following with your database details
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "Good_Database"
DB_PORT = "5432"


def fetch_data_from_db():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM main")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_data_to_db(data):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO main (age, name, hobby) VALUES (%s, %s, %s)", data)
    conn.commit()
    conn.close()


@app.route('/')
def get_data():
    data = fetch_data_from_db()
    return jsonify(data)

@app.route('/all_columns')
def get_all_columns():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'main'")
    columns = [row[0] for row in cur.fetchall()]
    conn.close()
    return jsonify(columns)

@app.route('/test')
def test():
    return ("test")

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()
    insert_data_to_db((int(data['column1']), data['column2'], data['column3']))
    return "Data added successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111)
