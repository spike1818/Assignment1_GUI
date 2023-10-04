import tkinter as tk
from tkinter import *
from close_login import close_login

def open_AAI():
    close_login()
    aai = tk.Tk()
    aai.geometry("1000x600")
    aai.title("AAI Page")
    welcome_message = Message(aai, width = 100, text = "Welcome 'name'")
    tracing_message = Message(aai, width = 100, text = "Tracing Methods")
    name_message = Message(aai, width = 150, text = "Name: 'first' and 'last'")
    DOB_message = Message(aai, width = 150, text = "DOB: DD/MM/YYYY'")
    exit_program = tk.Button(aai, text = "Exit", width = 10, command = aai.destroy)
    welcome_message.place(relx = 0.55, rely = 0, anchor = NE)
    tracing_message.place(relx = 0.80, rely = 0.325, anchor = NE)
    name_message.place(relx = 0.20, rely = 0.325, anchor = NW)
    DOB_message.place(relx = 0.20, rely = 0.4, anchor = NW)
    exit_program.place(relx = 1, rely = 1, anchor = SE)
    aai.mainloop()