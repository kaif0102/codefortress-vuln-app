from flask import Flask, request
import sqlite3

app = Flask(__name__)

# ❌ Hardcoded secret (TruffleHog will catch this)
AWS_SECRET_KEY = "AKIAFAKEKEY123456"

@app.route("/")
def home():
    return "Welcome to CodeFortress Vulnerable App"

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # ❌ SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login Successful"
    else:
        return "Login Failed"

# ❌ Debug enabled (security issue)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
