# Vitalis — Wellness Dashboard

Vitalis is a lightweight, full-stack health and wellness tracking application designed to help users log and visualize their daily diet, hydration, sleep, and physical activity. 

Built with a simple Flask backend, a MySQL database, and a beautiful, framework-free HTML/CSS/JS frontend, Vitalis offers a fully functional health dashboard with zero configuration overhead.

## 🚀 Features
- **User Authentication:** Secure registration and login system.
- **Health Tracking:** Log daily water intake, step count, and sleep duration.
- **Diet/Macro Logging:** Log individual meals, track total calories, and monitor macronutrients (protein, carbs, fats).
- **Interactive Dashboard:** Beautiful visual representations of your data using **Chart.js** (Line, Bar, and Doughnut charts).
- **Dynamic Profile & BMI:** Automatic BMI calculation and health goal tracking based on user metrics.
- **Responsive Design:** A sleek, modern user interface powered entirely by vanilla CSS and CSS variables.

## 🛠️ Tech Stack
- **Frontend:** HTML5, Vanilla CSS, Vanilla JavaScript, Chart.js
- **Backend:** Python, Flask, Flask-CORS
- **Database:** MySQL

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.x
- MySQL Server

### 1. Database Setup
Create a new MySQL database named `wellness_app`, then run the provided schema to set up the tables:
```sql
CREATE DATABASE wellness_app;
USE wellness_app;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    age INT,
    height FLOAT,
    weight FLOAT
);

CREATE TABLE health_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date DATE,
    water_intake FLOAT,
    steps INT,
    sleep_hours FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE diet_logs (
    diet_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date DATE,
    total_calories INT,
    protein FLOAT,
    carbs FLOAT,
    fats FLOAT,
    food_name VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```
*Note: Make sure to update the database credentials inside `app.py` and `seed.py` if your local MySQL configuration differs from `root` / `password`.*

### 2. Install Backend Dependencies
Create a virtual environment and install the required pip packages using the provided requirements file:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Load Sample Data (Optional)
If you'd like to test out the dashboard with historical dummy data right out of the box, use the included seed script to automatically load 15 days of mocked logs into your database:
```bash
python seed.py
```

### 4. Run the Server
Launch the Flask API:
```bash
python app.py
```
The server will default to running on `http://127.0.0.1:5000`.

### 4. Launch the App
Simply open the `wellness_app.html` file in your preferred web browser to access the application! No node server required.

## 📸 Overview
![Dashboard Interface Visual]
Once logged in, users are greeted with a comprehensive dashboard that computes daily averages, compares progress over different time periods (weekly vs monthly bounds), and aggregates both dietary inputs and pedometer readings.
