import tkinter as tk
from tkinter import *
from AAI_screen import open_AAI
from AOO_screen import open_AOO
from VOO_screen import open_VOO
from VVI_screen import open_VVI

def open_profile():
    profile = tk.Tk()
    profile.geometry("1000x600")
    profile.title("Profile Page")
    welcome_message = Message(profile, width = 100, text = "Welcome 'name'")
    tracing_message = Message(profile, width = 100, text = "Tracing Methods")
    name_message = Message(profile, width = 150, text = "Name: 'first' and 'last'")
    DOB_message = Message(profile, width = 150, text = "DOB: DD/MM/YYYY'")
    sign_out = tk.Button(profile, text = "Sign Out", width = 10, command = profile.destroy)
    exit_program = tk.Button(profile, text = "Exit", width = 10, command = profile.destroy)
    aoo = tk.Button(profile, text = "AOO", width = 10, command = open_AOO)
    voo = tk.Button(profile, text = "VOO", width = 10, command = open_VOO)
    aai = tk.Button(profile, text = "AAI", width = 10, command = open_AAI)
    vvi = tk.Button(profile, text = "VVI", width = 10, command = open_VVI)
    welcome_message.place(relx = 0.55, rely = 0, anchor = NE)
    tracing_message.place(relx = 0.80, rely = 0.325, anchor = NE)
    name_message.place(relx = 0.20, rely = 0.325, anchor = NW)
    DOB_message.place(relx = 0.20, rely = 0.4, anchor = NW)
    sign_out.place(relx = 1, rely = 0, anchor = NE)
    exit_program.place(relx = 1, rely = 1, anchor = SE)
    aoo.place(relx = 0.75, rely = 0.4, anchor = CENTER)
    voo.place(relx = 0.75, rely = 0.45, anchor = CENTER)
    aai.place(relx = 0.75, rely = 0.5, anchor = CENTER)
    vvi.place(relx = 0.75, rely = 0.55, anchor = CENTER)
    profile.mainloop()

if __name__ == "__main__":
    open_profile()
