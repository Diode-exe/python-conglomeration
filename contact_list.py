import sqlite3

# Connect to database
conn = sqlite3.connect("contact_list.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    number TEXT NOT NULL
)
""")
conn.commit()

# Ask the user what to do
action = input("1 to search contacts, 2 to create a new contact, 3 to view all contacts: ")

if action == "1":
    name = input("Enter the contact name to search: ")
    number = input("Enter the contact number to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name = ? AND number = ?", (name, number))
    result = cursor.fetchone()
    if result:
        print("Contact found:", result)
    else:
            print("No contact found with the given details.")
elif action == "2":
    name = input("Contact name: ")
    number = input("Contact number: ")

    cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    conn.commit()
    print("Contact created successfully")
elif action == "3":
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    for contact in results:
        print(contact)
else:
     print("Invalid selection! Exiting...")