import tkinter as tk
from welcome_screen import *
from tkinter import messagebox
from database import *
db = database()

 #creates a new user and adds their information to database
def create_acct():
    #handles creating a new user after the "create account" is pressed
    def new_user():
        if not(firstname_entry.get()):
            messagebox.showinfo(title="Account Creation Error",message="Enter a valid first name.")
        elif not(lastname_entry.get()):
            messagebox.showinfo(title="Account Creation Error",message="Enter a valid last name.")
        elif not(new_username_entry.get()):
            messagebox.showinfo(title="Account Creation Error",message="Enter a valid username.")
        elif len(new_username_entry.get()) < 4:
             messagebox.showinfo(title="Account Creation Error",message="Username must be at least 4 characters.")
        elif not(new_password_entry.get()):
            messagebox.showinfo(title="Password Creation Error",message="Enter a valid password.")
        elif new_password_entry.get()!=confirm_password_entry.get():
            messagebox.showinfo(title="Password Creation Error",message="Password entries do not match.")
        elif len(new_password_entry.get()) < 8:
            messagebox.showinfo(title="Password Creation Error",message="Password must be at least 8 characters")
        else:
            #check usernames
            usernameExists = False
            logins = db.query()
            count = 0
            for login in logins:
                count += 1
                if (new_username_entry.get() == login[0]):
                    usernameExists = True
                    messagebox.showinfo(title="Username Creation Error",message="Username already exists.")
            if usernameExists:
                messagebox.showinfo(title="Username Creation Error",message="Username already exists.")
            elif count > 10:
                messagebox.showinfo(title="Account Creation Error",message="Too many existing users.")
            
            else:
                db.submit(new_username_entry.get(),new_password_entry.get(),firstname_entry.get(),lastname_entry.get())
                messagebox.showinfo(title="Account Creation Success",message="Account creation successful.")
                create_window.destroy()
        
    #window
    create_window = tk.Tk()
    create_window.title("Create Account")
    create_window.geometry('600x450')
    create_window.configure(bg='#4863A0')

    #frame to hold the widgets
    create_frame = tk.Frame(create_window, bg='#4863A0')

    #create widgets
    create_acct_label = tk.Label(create_frame, text="Create Account", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
    firstname_label = tk.Label(create_frame, text="First Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    lastname_label = tk.Label(create_frame, text="Last Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    new_username_label = tk.Label(create_frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    new_password_label = tk.Label(create_frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    confirm_password_label = tk.Label(create_frame, text="Confirm Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    firstname_entry = tk.Entry(create_frame, font=("Arial", 12))
    lastname_entry = tk.Entry(create_frame, font=("Arial", 12))
    new_username_entry = tk.Entry(create_frame, font=("Arial", 12))
    new_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
    confirm_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
    create_acct_button = tk.Button(create_frame, text="Create Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=new_user)
    back_button = tk.Button(create_frame, text="Back", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=create_window.destroy)

    #place widgets
    create_acct_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
    firstname_label.grid(row=1, column=0)
    lastname_label.grid(row=2, column=0)
    new_username_label.grid(row=3, column=0) 
    new_password_label.grid(row=4, column=0)
    confirm_password_label.grid(row=5, column=0)
    firstname_entry.grid(row=1,column=1, pady=10)
    lastname_entry.grid(row=2, column=1, pady=10)
    new_username_entry.grid(row=3, column=1, pady=10) #spacing will affect everything in the same row
    new_password_entry.grid(row=4, column=1, pady=10) 
    confirm_password_entry.grid(row=5, column=1, pady=10, padx=5)
    create_acct_button.grid(row=6, column=0, columnspan=2, pady=10)
    back_button.grid(row=7,column=0, columnspan=2)

    create_frame.pack() #pack is responsive by default

    create_window.mainloop() #infinite loop that executes the app