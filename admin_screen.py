import tkinter as tk
from tkinter import *
from tkinter import messagebox
from database import *

window = tk.Tk()
window.title("Admin Setting")
window.geometry('500x400')
window.configure(bg='#4863A0')
        
#print records
def show_users():
    print_records = ''
    records = query()
    for record in records:
        print_records+= str(record[0])+"\n"

    query_label = Label(admin_frame, text = print_records, bg='#4863A0', fg='#FFFFFF')
    query_label.grid(row=4, column=0, columnspan = 2)

#frame for the widgets--makes it responsive when you change window size
admin_frame = tk.Frame(bg='#4863A0')

#make widgets
delete_user_entry = tk.Entry(admin_frame, font=("Arial", 12))
delete_user_label = tk.Label(admin_frame, text="Enter Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
delete_user_button = tk.Button(admin_frame, text="Delete User", bg='#FFFFFF', fg='#000000', font=("Arial", 10))
admin_label = tk.Label(admin_frame, text="Admin Settings", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 20))
show_users_button = tk.Button(admin_frame, text="Show Usernames", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=show_users)

#place widgets
admin_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
delete_user_entry.grid(row=1, column=1, padx=10)
delete_user_label.grid(row=1, column=0)
delete_user_button.grid(row=2, column=0, columnspan=2, pady=10)
show_users_button.grid(row=3, column=0, columnspan=2, pady=10)


admin_frame.pack() #pack is responsive by default

window.mainloop() #infinite loop that executes the app (stops when window is closed)