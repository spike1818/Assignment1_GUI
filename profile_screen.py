import tkinter as tk
from tkinter import *
profile = tk.Tk()
profile.title("Profile Page")
welcome_message = Message(profile, width = 100, text = "Welcome 'name'")
sign_out = tk.Button(profile, text = "Sign Out", width = 10, command = profile.destroy)
exit_program = tk.Button(profile, text = "Exit", width = 10, command = profile.destroy)
aoo = tk.Button(profile, text = "AOO", width = 10, command = profile.destroy)
voo = tk.Button(profile, text = "VOO", width = 10, command = profile.destroy)
aai = tk.Button(profile, text = "AAI", width = 10, command = profile.destroy)
vvi = tk.Button(profile, text = "VVI", width = 10, command = profile.destroy)
welcome_message.grid(row = 0, column = 1)
sign_out.grid(row = 0, column = 2)
exit_program.grid(row = 1, column = 2)
aoo.grid(row = 3, column = 1)
voo.grid(row = 3, column = 2)
aai.grid(row = 3, column = 3)
vvi.grid(row = 3, column = 4)
profile.mainloop()