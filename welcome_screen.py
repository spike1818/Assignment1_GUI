import tkinter as tk
from tkinter import *
from tkinter import messagebox

#make the window
window = tk.Tk()
window.title("Login")
window.geometry('340x400')
window.configure(bg='#4863A0')

#frame for the widgets--makes it responsive when you change window size
frame = tk.Frame(bg='#4863A0')

#make widgets
login_label = tk.Label(frame, text="Welcome", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 30))
username_label = tk.Label(frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 12))
password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
login_button = tk.Button(frame, text="Login", bg='#FFFFFF', fg='#000000', font=("Arial", 10))
#new_acct_button = tk.Button(window, text="Create New Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10))

#place widgets
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0) 
password_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1, pady=20) #spacing will affect everything in the same row
password_entry.grid(row=2, column=1, pady=20) 
login_button.grid(row=3, column=0, columnspan = 2, pady=30)
#new_acct_button.grid(row=4, column=0, columnspan = 2)

frame.pack() #pack is responsive by default

window.mainloop() #infinite loop that executes the app




#trying out stuff
# splash_screen = Tk()
# splash_screen.geometry("500x500")

# splash_label = Label(splash_screen, text="Welcome!", font=100)
# splash_label.pack()

# def main():
#     splash_screen.destroy()
#     welcome = tk.Tk()
#     Label(welcome, text="Username").grid(row=0)
#     Label(welcome, text="Password").grid(row=1)
#     entry1 = Entry(welcome)
#     entry2 = Entry(welcome)
#     entry1.grid(row=0, column=1)
#     entry2.grid(row=1, column=1)

# splash_screen.after(3000, main)
# mainloop()