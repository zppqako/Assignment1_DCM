import customtkinter
import sqlite3
import hashlib
import bcrypt
from tkinter import*
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("700x400")

# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         username TEXT NOT NULL,
#         password TEXT NOT NULL)''')
users = {}

# def register():
#     username = entry1.get()
#     password = entry2.get()
#     if username != '' and password != '':
#         cursor.execute('SELECT username FROM users WHERE username=?', [username])
#         if cursor.fetchone() is not None:
#             messagebox.showerror('Error', 'Username already exists.')
#         else:
#             encoded_password = password.encode('utf-8')
#             hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
#             cursor.execute('INSERT INTO users VALUES (?, ?)', [username,hashed_password])
#             conn.commit()
#             messagebox.showinfo('Success', 'Account has been created.')
#     elif username == '' and password == '':
#         messagebox.showerror('Error', 'Enter all data.')


def save_users():
    with open("users.txt", 'w') as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

def load_users():
    try:
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        pass

def register():
    username = entry1.get()
    password = entry2.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror('Error', 'Enter all data.')
        return
    if username in users:
        messagebox.showerror('Error', 'Username already exists.')
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    save_users()
    messagebox.showinfo('Success', 'Account has been created.')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

def login():
    username = entry1.get()
    password = entry2.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror('Error', 'Enter all data.')
        return
    if username not in users:
        messagebox.showerror('Error', 'User does not exist.')
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users[username] == hashed_password:
        messagebox.showinfo('Success', 'Login successfully')
        print("1")
    else:
        messagebox.showerror('Error', 'Password is not correct.')



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pacemaker Login System", font=('Arial', 18))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, command = login, text="Login", cursor = 'hand2')
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, command = register, text="Register here", cursor = 'hand2')
button2.pack(pady=12, padx=10)



root.mainloop()
