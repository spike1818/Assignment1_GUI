import tkinter as tk
from tkinter import *

def open_AOO():
    aoo = tk.Tk()
    aoo.geometry("500x400")
    aoo.configure(bg='#4863A0')
    aoo.title("aoo Page")
    aoo_middleframe = tk.Frame(aoo, bg = '#4863A0')
    welcome_message = tk.Label(aoo_middleframe, text = "AOO", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    welcome_message.grid(row = 0, column = 0)
    aoo_middleframe.pack()
    aoo.mainloop()
