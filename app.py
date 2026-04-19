from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import os

# ── DB CONNECTION HELPER ──────────────────────
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST", "localhost"),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", "#A2r7y3a6"),
        database=os.getenv("MYSQLDATABASE", "wellness_app"),
        port=int(os.getenv("MYSQLPORT", 3306))
    )

# ── HOME ───────────────────────────────────
@app.route("/")
def home():
    return "Wellness App Backend Running!"

# ── REGISTER ───────────────────────────────
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    try:
        name = data["name"]
        email = data["email"]
        password = data["password"]
        age = data["age"]
        height = data["height"]
        weight = data["weight"]

        db = get_db_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO users (name, email, password, age, height, weight)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, password, age, height, weight))
        db.commit()
        cursor.close()
        db.close()

        return jsonify({"message": "User registered successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ── LOGIN  ────────────────────────
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data["email"]
    password = data["password"]

    db = get_db_connection()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()

    if user:
        return jsonify({
            "message": "Login successful!",
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "age": user[4],
            "height": user[5],
            "weight": user[6]
        })
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# ── ADD HEALTH LOG ─────────────────────────
@app.route("/health-log", methods=["POST"])
def add_health_log():
    data = request.json

    try:
        db = get_db_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO health_logs (user_id, date, water_intake, steps, sleep_hours)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data["user_id"],
            data["date"],
            data["water_intake"],
            data["steps"],
            data["sleep_hours"]
        ))
        db.commit()
        
        cursor.close()
        db.close()

        return jsonify({"message": "Health log added successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ── ADD DIET LOG  ─
@app.route("/diet-log", methods=["POST"])
def add_diet_log():
    data = request.json

    try:
        db = get_db_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO diet_logs 
        (user_id, date, food_name, total_calories, protein, carbs, fats)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data["user_id"],
            data["date"],
            data["food_name"],
            data["total_calories"],
            data["protein"],
            data["carbs"],
            data["fats"]
        ))
        db.commit()
        
        cursor.close()
        db.close()

        return jsonify({"message": "Diet log added successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ── DASHBOARD  ─
@app.route("/dashboard/<int:user_id>", methods=["GET"])
def get_dashboard(user_id):

    db = get_db_connection()
    cursor = db.cursor()
    # Health logs
    cursor.execute("""
        SELECT date, water_intake, steps, sleep_hours 
        FROM health_logs 
        WHERE user_id = %s
    """, (user_id,))
    health_data = []
    for row in cursor.fetchall():
        d = row[0]
        date_str = d.strftime('%Y-%m-%d') if hasattr(d, 'strftime') else str(d)
        health_data.append((date_str,) + row[1:])

    # Diet logs 
    cursor.execute("""
        SELECT date, total_calories, protein, carbs, fats, food_name
        FROM diet_logs 
        WHERE user_id = %s
    """, (user_id,))
    diet_data = []
    for row in cursor.fetchall():
        d = row[0]
        date_str = d.strftime('%Y-%m-%d') if hasattr(d, 'strftime') else str(d)
        diet_data.append((date_str,) + row[1:])
        
    cursor.close()
    db.close()

    return jsonify({
        "health_logs": health_data,
        "diet_logs": diet_data
    })


# ── RUN ────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

# terminal : python app.py for starting flask server