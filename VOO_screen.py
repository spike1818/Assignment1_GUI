import tkinter as tk
from tkinter import *

def open_VOO():
    voo = tk.Tk()
    voo.geometry("1000x600")
    voo.title("voo Page")
    welcome_message = Message(voo, width = 100, text = "Welcome 'name'")
    tracing_message = Message(voo, width = 100, text = "Tracing Methods")
    name_message = Message(voo, width = 150, text = "Name: 'first' and 'last'")
    DOB_message = Message(voo, width = 150, text = "DOB: DD/MM/YYYY'")
    exit_program = tk.Button(voo, text = "Exit", width = 10, command = voo.destroy)
    welcome_message.place(relx = 0.55, rely = 0, anchor = NE)
    tracing_message.place(relx = 0.80, rely = 0.325, anchor = NE)
    name_message.place(relx = 0.20, rely = 0.325, anchor = NW)
    DOB_message.place(relx = 0.20, rely = 0.4, anchor = NW)
    exit_program.place(relx = 1, rely = 1, anchor = SE)
    voo.mainloop()