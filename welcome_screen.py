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
db = database()

def open():

    def reopen():
        window.destroy()
        create_acct()
        open()

    def login():
        logins = db.query()
        loginSuccessful = False
        global login_name
        global login_id
        global login_LRL
        global login_URL
        global login_AA
        global login_APW
        global login_VA
        global login_VPW 
        global login_VRP
        global login_ARP
        global login_M
  
        for login in logins:
            if username_entry.get()==login[0] and password_entry.get()==login[1] and username_entry.get() == "admin":

                admin_screen()
                loginSuccessful = True
                window.destroy()
                open_profile()
                open()

            elif username_entry.get()==login[0] and password_entry.get()==login[1]: #need to pull from database
                login_name = login_name = login[2] + " " + login[3]
                login_id = login[13]
                login_LRL = login[4]
                login_URL = login[5]
                login_AA = login[6]
                login_APW = login[7]
                login_ARP = login[10]
                login_VA = login[8]
                login_VPW = login[9]
                login_VRP = login[11]
                login_M = login[12]

                loginSuccessful = True
                window.destroy()
                open_profile()
                open()
        if (not loginSuccessful):
            messagebox.showinfo(title="Invalid Login",message="Your login credentials are invalid.") #**need a way to link this to create account

    #make the window
    window = tk.Tk()
    window.title("Login")
    window.geometry('500x400')
    window.configure(bg='#4863A0')
        
    #frame for the widgets--makes it responsive when you change window size
    frame = tk.Frame(bg='#4863A0')

    #make widgets
    login_label = tk.Label(frame, text="Login", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
    username_label = tk.Label(frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    password_label = tk.Label(frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 12))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
    login_button = tk.Button(frame, text="Login", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=login)
    new_acct_button = tk.Button(frame, text="Create New Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=reopen)

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