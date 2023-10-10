import tkinter as tk
from tkinter import *
from tkinter import messagebox
from open_profile import open_profile #imports profile screen to welcome screen file
from database import *
from admin_screen import admin_screen
from create_account_screen import *

#simple example for demonstrative purposes
admin_username = "admin" 
admin_password = "password"

def open():
    # #checks against database for user credentials
    def login():
        logins = query()
        loginSuccessful = False

        for login in logins:
            print(login)
            if username_entry.get()==login[0] and password_entry.get()==login[1]: #need to pull from database
                loginSuccessful = True
                window.destroy()
                open_profile()
                open()
        if username_entry.get()==admin_username and password_entry.get()==admin_password:
            window.destroy()
            admin_screen()
            open()
        elif (not loginSuccessful):
            messagebox.showinfo(title="Invalid Login",message="Your login credentials are invalid.") #**need a way to link this to create account

    #make the window
    window = tk.Tk()
    window.title("Login")
    window.geometry('500x400')
    window.configure(bg='#4863A0')
        
    #frame for the widgets--makes it responsive when you change window size
    frame = tk.Frame(bg='#4863A0')

    #make widgets
    login_label = tk.Label(frame, text="Login", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 30))
    username_label = tk.Label(frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    password_label = tk.Label(frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 12))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
    login_button = tk.Button(frame, text="Login", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=login)
    new_acct_button = tk.Button(frame, text="Create New Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=create_acct)

    #place widgets
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0) 
    password_label.grid(row=2, column=0)
    username_entry.grid(row=1, column=1, pady=10) #spacing will affect everything in the same row
    password_entry.grid(row=2, column=1, pady=20) 
    login_button.grid(row=3, column=0, columnspan=2)
    new_acct_button.grid(row=4, column=0, columnspan=2, pady=10)

    frame.pack() #pack is responsive by default

    window.mainloop() #infinite loop that executes the app (stops when window is closed)