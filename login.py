import sqlite3
import hashlib

# Connect to database
conn = sqlite3.connect("logonData.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def failedAttempt():
    print("Login failed: username or password is incorrect.")

# Ask the user what to do
action = input("1 to log in, 2 to create a new user, 3 if you forgot your password: ")

if action == "1":
    # LOGIN
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    password_hashed = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (name, password_hashed))
    result = cursor.fetchone()

    if result:
        print("Login successful!")
        loggedIn = 1
        
    else:
        failedAttempt()

elif action == "2":
    # CREATE NEW USER
    name = input("Choose a username: ")
    password = input("Choose a password: ")
    password_hashed = hash_password(password)

    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password_hashed))
    conn.commit()
    print("User created successfully")

elif action == "3":
    print("This option isn't implemented yet.")

else:
    print("Invalid option.")

# Close connection
conn.close()
if loggedIn == 1:
    print(f"Hello, {name}")