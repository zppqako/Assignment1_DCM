import customtkinter
import hashlib
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("700x400")

users = {}

def show_login_page():
    register_page.pack_forget()
    mode_page.pack_forget()
    login_page.pack()
def save_users():
    with open("users.txt", 'w') as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")
    register_page.pack_forget()
    mode_page.pack_forget()
    login_page.pack()

def load_users():
    try:
        with open("users.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        pass
    register_page.pack_forget()
    mode_page.pack_forget()
    login_page.pack()

def confirm():
    username = new_username.get()
    password = new_password.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror('Error', 'Username or password cannot be empty.')
        register_page.pack()
        return
    if username in users:
        messagebox.showerror('Error', 'Username already exists.')
        register_page.pack()
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    save_users()
    messagebox.showinfo('Success', 'Account has been created.')
    new_username.delete(0, 'end')
    new_password.delete(0, 'end')
    register_page.pack_forget()
    mode_page.pack_forget()
    login_page.pack()

def register():
    login_username.delete(0, 'end')
    login_password.delete(0, 'end')
    login_page.pack_forget()
    mode_page.pack_forget()
    register_page.pack()

def login():
    username = login_username.get()
    password = login_password.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror('Error', 'Username or password cannot be empty.')
        login_page.pack()
        return
    if username not in users:
        messagebox.showerror('Error', 'User does not exist.')
        login_username.delete(0, 'end')
        login_password.delete(0, 'end')
        login_page.pack()
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users[username] == hashed_password:
        messagebox.showinfo('Success', 'Login successfully')
        login_page.pack_forget()
        register_page.pack_forget()
        mode_page.pack()
    else:
        messagebox.showerror('Error', 'Password is not correct.')
        login_password.delete(0, 'end')
        login_page.pack()

def AOO():
    print("AOO")
    print("Test")
def VOO():
    print("VOO")
def AAI():
    print("AAI")
def VVI():
    print("VVI")

# login page
login_page = customtkinter.CTkFrame(master=root)
login_page.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=login_page, text="Pacemaker Login System", font=('Arial', 18))
label.pack(pady=12, padx=10)

login_username = customtkinter.CTkEntry(master=login_page, placeholder_text="Username")
login_username.pack(pady=12, padx=10)

login_password = customtkinter.CTkEntry(master=login_page, placeholder_text="Password", show="*")
login_password.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=login_page, command = login, text="Login", cursor ='hand2')
login_button.pack(pady=12, padx=10)

register_button = customtkinter.CTkButton(master=login_page, command = register, text="Register here", cursor ='hand2')
register_button.pack(pady=12, padx=10)

# register page
register_page = customtkinter.CTkFrame(master=root)
register_page.pack(pady=20, padx=60)#, fill="both", expand = True)
# new user name entry
new_username = customtkinter.CTkEntry(master=register_page, placeholder_text="New Username")
new_username.pack(pady=12, padx=10)
# new user name entry
new_password = customtkinter.CTkEntry(master=register_page, placeholder_text="New Password")
new_password.pack(pady=12,padx=10)
# click button to comfirm
confirm_button = customtkinter.CTkButton(master=register_page, text="confirm", command=confirm)
confirm_button.pack(pady=12,padx=10)


# mode page
mode_page = customtkinter.CTkFrame(master=root)
mode_page.pack(pady=20, padx=60)#, fill="both", expand = True)
# output a label
label2 = customtkinter.CTkLabel(master=mode_page, text="Please select the mode of pacemaker")
label2.pack(pady=12, padx=10)
#AOO mode
AOO_button = customtkinter.CTkButton(master=mode_page, text="AOO", command=AOO)
AOO_button.pack(pady=12,padx=10)
#VOO mode
VOO_button = customtkinter.CTkButton(master=mode_page, text="VOO", command=VOO)
VOO_button.pack(pady=12,padx=10)
#AAI mode
AAI_button = customtkinter.CTkButton(master=mode_page, text="AAI", command=AAI)
AAI_button.pack(pady=12,padx=10)
#VVI mode
VVI_button = customtkinter.CTkButton(master=mode_page, text="VVI", command=VVI)
VVI_button.pack(pady=12,padx=10)

show_login_page()
root.mainloop()
