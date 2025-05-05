import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox

def connect_db():
    conn = sqlite3.connect("contact_list.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        number TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn, cursor


def gui_mode():
    conn, cursor = connect_db()

    def add_contact():
        name = simpledialog.askstring("Input", "Enter contact name:")
        number = simpledialog.askstring("Input", "Enter contact number:")
        if name and number:
            cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
            conn.commit()
            messagebox.showinfo("Success", "Contact added!")
        else:
            messagebox.showerror("Error", "Name and/or number cannot be empty.")

    def view_contacts():
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        contact_list = "\n".join([f"{id} - {name} - {number}" for id, name, number in results])
        messagebox.showinfo("Contacts", contact_list or "No contacts found.")
    
    def edit_contacts_by_name():
        old_name = simpledialog.askstring("Edit Contact", "Name to edit?")
        old_number = simpledialog.askstring("Edit Contact", "Number to edit?")

        # Search for the contact
        cursor.execute("SELECT * FROM contacts WHERE name = ? AND number = ?", (old_name, old_number))
        contact = cursor.fetchone()

        if contact:
            new_name = simpledialog.askstring("Edit Contact", f"New name (current: {contact[1]}):") or contact[1]
            new_number = simpledialog.askstring("Edit Contact", f"New number (current: {contact[2]}):") or contact[2]

            cursor.execute("UPDATE contacts SET name = ?, number = ? WHERE id = ?", (new_name, new_number, contact[0]))
            conn.commit()
            messagebox.showinfo("Success", "Contact updated!")
        else:
            messagebox.showerror("Error", "Contact not found.")

            simpledialog.showinfo("")
    def edit_contacts_by_id():
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()

        contact_id = simpledialog.askstring("Edit Contact", "Enter Contact ID:")

        # Check if the contact exists
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        contact = cursor.fetchone()

        if contact:
            new_name = simpledialog.askstring("New name", f"New name (current: {contact[1]}): ") or contact[1]
            new_number = simpledialog.askstring("New number", f"New number (current: {contact[2]}): ") or contact[2]

            if new_name and new_number:
                cursor.execute("UPDATE contacts SET name = ?, number = ? WHERE id = ?", (new_name, new_number, contact_id))
                conn.commit()
                print("Contact updated successfully.")
                messagebox.showinfo("Success!", "Contact updated successfully!")
            else:
                print("Name and/or number cannot be empty")
                messagebox.showinfo("Error", "Name and/or number cannot be empty")
        else:
            print("No contact found with that ID.")
            messagebox.showinfo("Error", "No contact found with that ID.")
        
    root = tk.Tk()
    root.title("Contact List")
    root.geometry("400x250") #Width x Height

    tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
    tk.Button(root, text="Edit Contacts by Name", command=edit_contacts_by_name).pack(pady=5)
    tk.Button(root, text="Edit Contacts by ID", command=edit_contacts_by_id).pack(pady=5)
    tk.Button(root, text="View All Contacts", command=view_contacts).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

    root.mainloop()
    conn.close()

# Main program
gui_mode()