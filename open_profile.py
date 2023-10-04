import tkinter as tk
from tkinter import *
from tkinter import messagebox
from AAI_screen import open_AAI
from AOO_screen import open_AOO
from VOO_screen import open_VOO
from VVI_screen import open_VVI

def open_profile():
    profile = tk.Tk()
    profile.geometry("500x400")
    profile.configure(bg='#4863A0')
    profile.title("Profile Page")
    profile_topframe = tk.Frame(profile, bg='#4863A0')
    profile_middleframe = tk.Frame(profile, bg='#4863A0')
    profile_bottomframe = tk.Frame(profile, bg='#4863A0')

    welcome_message = tk.Label(profile_topframe, text = "Welcome 'name'", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    tracing_message = tk.Label(profile_middleframe, text = "Tracing Methods", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    sign_out = tk.Button(profile_bottomframe, text = "Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = profile.destroy)
    exit_program = tk.Button(profile_bottomframe, text = "Exit", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = profile.destroy)
    aoo = tk.Button(profile_middleframe, text = "AOO", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_AOO)
    voo = tk.Button(profile_middleframe, text = "VOO", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_VOO)
    aai = tk.Button(profile_middleframe, text = "AAI", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_AAI)
    vvi = tk.Button(profile_middleframe, text = "VVI", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_VVI)
    
    welcome_message.grid(row=0, column=0, columnspan=6, sticky="news", pady = 40)

    tracing_message.grid(row=0, column=0)
    sign_out.grid(row=0, column=0)
    exit_program.grid(row=1, column=0)
    aoo.grid(row=1, column=0)
    voo.grid(row=2, column=0)
    aai.grid(row=3, column=0)
    vvi.grid(row=4, column=0)
    profile_middleframe.grid_rowconfigure(5, minsize=50)
    profile_topframe.pack()
    profile_middleframe.pack()
    profile_bottomframe.pack()
    profile.mainloop()

if __name__ == "__main__":
    open_profile()
