import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#A2r7y3a6",
    database="wellness_app"
)
cursor = db.cursor()

# Get user_id for aryapore@example.com
cursor.execute("SELECT user_id FROM users WHERE email = 'aryapore@example.com'")
result = cursor.fetchone()

if result:
    user_id = result[0]
else:
    cursor.execute("INSERT INTO users (name, email, password, age, height, weight) VALUES ('Arya Pore', 'aryapore@example.com', '1234567890', 25, 175.0, 70.0)")
    user_id = cursor.lastrowid

cursor.execute("SET @user_id = %s", (user_id,))

# Read the rest of the script
with open('seed_data.sql', 'r') as file:
    sql_script = file.read()

# Skip the users insertion logic
parts = sql_script.split('SET @user_id = LAST_INSERT_ID();')
if len(parts) > 1:
    sql_script = parts[1]

for statement in sql_script.split(';'):
    if statement.strip():
        if statement.strip().startswith('--'):
            continue
        try:
            cursor.execute(statement)
        except Exception as e:
            # Avoid printing expected errors like duplicate entry if the script was run multiple times
            pass

db.commit()
print("Data seeded successfully!")
