from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    content = request.form.get('content')
    risk_level = "Cao" if "lừa đảo" in content.lower() or "đặt cọc" in content.lower() or "hợp đồng" in content.lower() else "An toàn"
    result_text = f"Hệ thống đã phân tích nội dung. Phát hiện dấu hiệu rủi ro ở mức: {risk_level}."

    conn = get_db_connection()
    conn.execute('INSERT INTO scan_history (content, result, risk_level) VALUES (?, ?, ?)',
                 (content, result_text, risk_level))
    conn.commit()
    conn.close()

    return render_template('index.html', result=result_text, risk=risk_level, content=content)

if __name__ == '__main__':
    app.run(debug=True)