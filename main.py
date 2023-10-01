import tkinter as tk
from profile_screen import open_profile

root = tk.Tk()
button = tk.Button(root, width = 20, text = "Start!", command = open_profile)
button.pack()

root.mainloop()
