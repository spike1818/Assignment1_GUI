import tkinter as tk
from tkinter import *
from tkinter import messagebox
from profile_screen import open_profile #imports profile screen to welcome screen file

#simple example for demonstrative purposes
username = "alex" 
password = "321"

# #checks against database for user credentials
def login():
    if username_entry.get()==username and password_entry.get()==password: #need to pull from database
        messagebox.showinfo(title="Successful Login",message="You have successfully logged in.")
        open_profile()
    else:
        messagebox.showinfo(title="Invalid Login",message="Your login credentials are invalid.") #**need a way to link this to create account

#creates a new user and adds their information to database
def create_acct():  
    
    #handles creating a new user after the "create account" is pressed
    def new_user():
        if new_password_entry.get()!=confirm_password_entry.get():
            messagebox.showinfo(title="Password Creation Error",message="Password entries do not match.")
        elif new_username_entry.get()!=username:
            messagebox.showinfo(title="Account Creation Success",message="Account creation successful.")
        elif new_username_entry.get()==username:
            messagebox.showinfo(title="Username Creation Error",message="Username already exists.")
   
    #window
    create_window = tk.Toplevel(window) #child of login window
    create_window.title("Create Account")
    create_window.geometry('550x350')
    create_window.configure(bg='#4863A0')

    #frame to hold the widgets
    create_frame = tk.Frame(create_window, bg='#4863A0')

    #create widgets
    create_acct_label = tk.Label(create_frame, text="Create Account", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 30))
    new_username_label = tk.Label(create_frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    new_password_label = tk.Label(create_frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    confirm_password_label = tk.Label(create_frame, text="Confirm Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    new_username_entry = tk.Entry(create_frame, font=("Arial", 12))
    new_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
    confirm_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
    create_acct_button = tk.Button(create_frame, text="Create Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=new_user)

    #place widgets
    create_acct_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
    new_username_label.grid(row=1, column=0) 
    new_password_label.grid(row=2, column=0)
    confirm_password_label.grid(row=3, column=0)
    new_username_entry.grid(row=1, column=1, pady=10) #spacing will affect everything in the same row
    new_password_entry.grid(row=2, column=1, pady=10) 
    confirm_password_entry.grid(row=3, column=1, pady=10, padx=5)
    create_acct_button.grid(row=4, column=0, columnspan=2, pady=10)

    #push the create account button
        #redirect to login page
            #account creation is successful and user is added to database
            #account already exists
        #error message
            #passwords do not match

    create_frame.pack() #pack is responsive by default

    create_window.mainloop() #infinite loop that executes the app

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