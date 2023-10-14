import tkinter as tk
from tkinter import *

def open_AAI():
    aai = tk.Tk()
    aai.geometry("500x400")
    aai.configure(bg='#4863A0')
    aai.title("AAI Page")
    aai_middleframe = tk.Frame(aai, bg = '#4863A0')
    welcome_message = tk.Label(aai_middleframe, text = "AAI", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    backAAI = tk.Button(aai_middleframe, text = "Back", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = aai.destroy)
    welcome_message.grid(row = 0, column = 0)
    backAAI.grid(row = 1, column = 0)
    aai_middleframe.pack()
    
    aai.mainloop()