import tkinter as tk
from tkinter import messagebox
from AAI_screen import open_AAI
from AOO_screen import open_AOO
from VOO_screen import open_VOO
from VVI_screen import open_VVI
from change_settings import change_settings
import welcome_screen

def open_profile():
    profile = tk.Tk()
    profile.geometry("500x450")
    profile.configure(bg='#4863A0')
    profile.title("Profile Page")
    profile_topframe = tk.Frame(profile, bg='#4863A0')
    profile_middleframe = tk.Frame(profile, bg='#4863A0')
    profile_bottomframe = tk.Frame(profile, bg='#4863A0')

    message = "Welcome," + " " + welcome_screen.login_name #matches username entered to name stored in database

    #create info for corner of screen
    connection_message = tk.Label(profile, text="Connection Status: Pacemaker not connected\nPacemaker version: 1\nDate of implant: 01/01/2023", bg='#4863A0', fg='#FFFFFF', font=("Arial",8))
    welcome_message = tk.Label(profile_topframe, text = message, bg='#4863A0', fg='#FFFFFF', font=("Georgia", 16))
    tracing_message = tk.Label(profile_middleframe, text = "Tracing Methods", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 16))
    sign_out = tk.Button(profile_bottomframe, text = "Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = profile.destroy)
    aoo = tk.Button(profile_middleframe, text = "AOO", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_AOO)
    voo = tk.Button(profile_middleframe, text = "VOO", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_VOO)
    aai = tk.Button(profile_middleframe, text = "AAI", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_AAI)
    vvi = tk.Button(profile_middleframe, text = "VVI", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = open_VVI)
    Profile_edit = tk.Button(profile_bottomframe, text = "Profile Edit", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = change_settings)
    
    connection_message.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tk.SE)
    welcome_message.grid(row=0, column=0, columnspan=6, sticky="news", pady = 20)
    tracing_message.grid(row=0, column=0, pady=10)
    Profile_edit.grid(row=0, column = 0)
    sign_out.grid(row=1, column=0)
    aoo.grid(row=1, column=0)
    voo.grid(row=2, column=0, pady=10)
    aai.grid(row=3, column=0)
    vvi.grid(row=4, column=0, pady=10)
    profile_middleframe.grid_rowconfigure(5, minsize=50)
    profile_topframe.pack()
    profile_middleframe.pack()
    profile_bottomframe.pack()

    #later will check whether pacemaker is connected before displaying error message
    messagebox.showinfo(title="Connection Error",message="Pacemaker is not connected.")

    profile.mainloop()