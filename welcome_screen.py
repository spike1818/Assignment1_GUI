import tkinter as tk
from tkinter import *
from token import SLASH

splash_screen = Tk()
# splash_screen.title("Welcome")
splash_screen.geometry("500x500")

splash_label = Label(splash_screen, text="Welcome!", font=100)
splash_label.pack()

def main():
    splash_screen.destroy()
    welcome = tk.Tk()
    Label(welcome, text="Username").grid(row=0)
    Label(welcome, text="Password").grid(row=1)
    entry1 = Entry(welcome)
    entry2 = Entry(welcome)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

splash_screen.after(3000, main)
mainloop()