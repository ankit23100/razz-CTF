from flask import Flask, request, render_template
import os
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'challuser'),
    'password': os.getenv('DB_PASSWORD', 'challpass'),
    'database': os.getenv('DB_NAME', 'challenge_db'),
    'autocommit': True,
}

def get_db_conn():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form.get('username', '')
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
        cur.execute(query)
        results = cur.fetchall()
    except Exception as e:
        conn.close()
        return render_template('result.html', error=str(e), rows=None)
    conn.close()
    return render_template('result.html', rows=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
