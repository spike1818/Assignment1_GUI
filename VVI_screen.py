import tkinter as tk
from tkinter import *

def open_VVI():
    vvi = tk.Tk()
    vvi.geometry("500x400")
    vvi.configure(bg='#4863A0')
    vvi.title("VVI Page")
    vvi_middleframe = tk.Frame(vvi, bg = '#4863A0')
    welcome_message = tk.Label(vvi_middleframe, text = "VVI", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    backVVI = tk.Button(vvi_middleframe, text = "Back", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = vvi.destroy)
    welcome_message.grid(row = 0, column = 0)
    backVVI.grid(row=1, column=0)
    vvi_middleframe.pack()
    vvi.mainloop()