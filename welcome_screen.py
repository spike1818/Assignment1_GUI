import tkinter as tk
from tkinter import *
welcome = tk.Tk()
Label(welcome, text="Username").grid(row=0)
Label(welcome, text="Password").grid(row=1)
entry1 = Entry(welcome)
entry2 = Entry(welcome)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
mainloop()