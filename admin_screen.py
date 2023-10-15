import tkinter as tk
from tkinter import *
from tkinter import messagebox
from database import *


def admin_screen():
    admin_window = tk.Tk()
    admin_window.title("Admin Settings")
    admin_window.geometry('500x600')
    admin_window.configure(bg='#4863A0')
    
    #get admin id number
    records = query()
    for record in records:
        if(record[0] == "admin"):
            admin_id = record[13]
    
    #print records
    def show_users():
        print_records = ''
        records = query()
        for record in records:
            if record[0] == "admin":
                pass
            else:
                print_records+= str(record[0])+", "+str(record[13])+"\n"

        query_label = Label(admin_frame, text = print_records, bg='#4863A0', fg='#FFFFFF')
        query_label.grid(row=4, column=0, columnspan = 2)

    #frame for the widgets--makes it responsive when you change window size
    admin_frame = tk.Frame(admin_window, bg='#4863A0')

    #make widgets
    delete_user_entry = tk.Entry(admin_frame, font=("Arial", 12))
    delete_user_label = tk.Label(admin_frame, text="Enter ID", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    delete_user_button = tk.Button(admin_frame, text="Delete User", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=lambda: delete(delete_user_entry.get()))
    admin_label = tk.Label(admin_frame, text="Admin Settings", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
    show_users_button = tk.Button(admin_frame, text="Show Usernames/IDs", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=show_users)
    password_entry = tk.Entry(admin_frame, font=("Arial",12))
    password_label = tk.Label(admin_frame, text="Admin Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    change_password_button = tk.Button(admin_frame, text="Change Password", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command= lambda: changePassword(admin_id,password_entry.get()))
    signout_button = tk.Button(admin_frame, text="Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=admin_window.destroy)

    #place widgets
    admin_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
    delete_user_entry.grid(row=1, column=1, padx=10)
    delete_user_label.grid(row=1, column=0)
    delete_user_button.grid(row=2, column=0, columnspan=2, pady=10)
    show_users_button.grid(row=3, column=0, columnspan=2, pady=10)
    password_entry.grid(row=7, column=1, padx=10)
    password_label.grid(row=7,column=0)
    change_password_button.grid(row=8, column=0, columnspan=2, pady=10)
    signout_button.grid(row=9, column=0, columnspan=2)

    records = query()
    for record in records:
        if record[0] == "admin":
            current_password = record[1]
            password_entry.insert(0, current_password)

    admin_frame.pack() #pack is responsive by default

    admin_window.mainloop() #infinite loop that executes the app (stops when window is closed)