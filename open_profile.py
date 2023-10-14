import tkinter as tk
from tkinter import messagebox
from AAI_screen import open_AAI
from AOO_screen import open_AOO
from VOO_screen import open_VOO
from VVI_screen import open_VVI
from change_settings import change_settings
import welcome_screen
import database

def open_profile():
    profile = tk.Tk()
    profile.geometry("500x500")
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
    Profile_edit = tk.Button(profile_bottomframe, text = "Profile Edit", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = lambda: database.edit(str(welcome_screen.login_id)))

        #pacing modes
    pulserate_acc_title = tk.Label(profile_middleframe, text="Pulse Rate: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulsewidth_acc_title = tk.Label(profile_middleframe, text="Pulse Width: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseamp_acc_title = tk.Label(profile_middleframe, text="Pulse Amplitude: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    sensingsense_acc_title = tk.Label(profile_middleframe, text="Sensing Sensitivity: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pacingmode_acc_title = tk.Label(profile_middleframe, text="Pacing Mode: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    refracper_acc_title = tk.Label(profile_middleframe, text="Refractory Period: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

        #acc title alignment
    pulserate_acc_title.grid(row=1,column=0)
    pulsewidth_acc_title.grid(row=2,column=0)
    pulseamp_acc_title.grid(row=3,column=0)
    sensingsense_acc_title.grid(row=4,column=0)
    pacingmode_acc_title.grid(row=5,column=0)
    refracper_acc_title.grid(row=6,column=0)
    
    connection_message.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tk.SE)
    welcome_message.grid(row=0, column=0, columnspan=6, sticky="news", pady = 20)
    tracing_message.grid(row=1, column=2, pady=10)
    Profile_edit.grid(row=0, column = 0)
    sign_out.grid(row=1, column=0, pady=10)
    aoo.grid(row=2, column=2)
    voo.grid(row=3, column=2, pady=10)
    aai.grid(row=4, column=2)
    vvi.grid(row=5, column=2, pady=10)
    profile_middleframe.grid_rowconfigure(10, minsize=50)
    profile_middleframe.grid_columnconfigure(1, min = 150)
    profile_topframe.pack()
    profile_middleframe.pack()
    profile_bottomframe.pack()

    #later will check whether pacemaker is connected before displaying error message
    messagebox.showinfo(title="Connection Error",message="Pacemaker is not connected.")

    profile.mainloop()
