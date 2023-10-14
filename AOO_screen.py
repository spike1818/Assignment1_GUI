import tkinter as tk
from tkinter import *

def open_AOO():
    aoo = tk.Tk()
    aoo.geometry("500x400")
    aoo.configure(bg='#4863A0')
    aoo.title("AOO Page")
    aoo_middleframe = tk.Frame(aoo, bg = '#4863A0')
    welcome_message = tk.Label(aoo_middleframe, text = "AOO", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    backAOO = tk.Button(aoo_middleframe, text = "Back", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = aoo.destroy)
    welcome_message.grid(row = 0, column = 0)
    backAOO.grid(row = 1, column = 0)
    aoo_middleframe.pack()
    aoo.mainloop()