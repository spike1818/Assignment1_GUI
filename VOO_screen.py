import tkinter as tk
from tkinter import *

def open_VOO():
    voo = tk.Tk()
    voo.geometry("500x400")
    voo.configure(bg='#4863A0')
    voo.title("voo Page")
    voo_middleframe = tk.Frame(voo, bg = '#4863A0')
    welcome_message = tk.Label(voo_middleframe, text = "VOO", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    welcome_message.grid(row = 0, column = 0)
    voo_middleframe.pack()
    voo.mainloop()