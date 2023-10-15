import tkinter as tk
from tkinter import messagebox
from AAI_screen import open_AAI
from AOO_screen import open_AOO
from VOO_screen import open_VOO
from VVI_screen import open_VVI
import welcome_screen
from database import *

def open_profile():
    profile = tk.Tk()
    profile.geometry("600x650")
    profile.configure(bg='#4863A0')
    profile.title("Profile Page")
    profile_topframe = tk.Frame(profile, bg='#4863A0')
    profile_middleframe = tk.Frame(profile, bg='#4863A0')
    profile_bottomframe = tk.Frame(profile, bg='#4863A0')

    def reopen():
        profile.destroy()
        edit(str(welcome_screen.login_id))
        open_profile()
        
    message = "Welcome," + " " + welcome_screen.login_name #matches username entered to name stored in database
    LRLmessage = "Lower Rate Limit: " + str(welcome_screen.login_LRL)
    URLmessage = "Upper Rate Limit: " + str(welcome_screen.login_URL)
    APWmessage = "Atrial Pulse Width: " + str(welcome_screen.login_APW)
    AAmessage = "Atrial amplitude: " + str(welcome_screen.login_AA)
    ARPmessage = "ARP: " + str(welcome_screen.login_ARP)
    VPWmessage = "Ventricular Pulse Width: " + str(welcome_screen.login_VPW)
    VAmessage = "Vntricular Amplitude: " + str(welcome_screen.login_VA)
    VRPmessage = "VRP: " + str(welcome_screen.login_VRP)
    Mmessage = "Pacing Mode: " + str(welcome_screen.login_M)

    #create info for corner of screen
    connection_message = tk.Label(profile, text="Connection Status: Pacemaker not connected\nPacemaker version: 1\nDate of implant: 01/01/2023", bg='#4863A0', fg='#FFFFFF', font=("Arial",8))
    welcome_message = tk.Label(profile_topframe, text = message, bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    tracing_message = tk.Label(profile_middleframe, text = "Tracing Methods", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
    sign_out = tk.Button(profile_bottomframe, text = "Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = profile.destroy)
    aoo = tk.Button(profile_middleframe, text = "AOO", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = open_AOO)
    voo = tk.Button(profile_middleframe, text = "VOO", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = open_VOO)
    aai = tk.Button(profile_middleframe, text = "AAI", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = open_AAI)
    vvi = tk.Button(profile_middleframe, text = "VVI", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = open_VVI)
   
    profile_edit = tk.Button(profile_bottomframe, text = "Edit Profile", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = reopen)

    #pacing modes
    pulseratelow_acc_title = tk.Label(profile_middleframe, text= LRLmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseratehigh_acc_title = tk.Label(profile_middleframe, text= URLmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulsewidth_arial_title = tk.Label(profile_middleframe, text= APWmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseamp_arial_title = tk.Label(profile_middleframe, text= AAmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulsewidth_ventr_title = tk.Label(profile_middleframe, text= VPWmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseamp_ventr_title = tk.Label(profile_middleframe, text= VAmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    VRP_acc_title = tk.Label(profile_middleframe, text= VRPmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pacingmode_acc_title = tk.Label(profile_middleframe, text= Mmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ARP_acc_title = tk.Label(profile_middleframe, text= ARPmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

        #acc title alignment
    pulseratelow_acc_title.grid(row=2,column=0)
    pulseratehigh_acc_title.grid(row=3,column=0)
    pulsewidth_arial_title.grid(row=4,column=0)
    pulseamp_arial_title.grid(row=5,column=0)
    pulsewidth_ventr_title.grid(row=6,column=0)
    pulseamp_ventr_title.grid(row=7,column=0)
    VRP_acc_title.grid(row=8,column=0)
    pacingmode_acc_title.grid(row=10,column=0)
    ARP_acc_title.grid(row=9,column=0)
    
    connection_message.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tk.SE)
    welcome_message.grid(row=0, column=0, columnspan=6, sticky="news", pady = 20)
    tracing_message.grid(row=1, column=2, pady=10)
    profile_edit.grid(row=0, column = 0)
    sign_out.grid(row=1, column=0, pady=10)
    aoo.grid(row=2, column=2)
    voo.grid(row=3, column=2, pady=10)
    aai.grid(row=4, column=2)
    vvi.grid(row=5, column=2, pady=10)

    #fixing row spacing
    profile_middleframe.grid_rowconfigure(6, minsize=35)
    profile_middleframe.grid_rowconfigure(7, minsize=35)
    profile_middleframe.grid_rowconfigure(8, minsize=35)
    profile_middleframe.grid_rowconfigure(9, minsize=35)
    profile_middleframe.grid_rowconfigure(10, minsize=35)
    profile_middleframe.grid_rowconfigure(11, minsize=35) 
    profile_middleframe.grid_rowconfigure(12, minsize=50)
    profile_middleframe.grid_columnconfigure(1, min = 150)
    profile_topframe.pack()
    profile_middleframe.pack()
    profile_bottomframe.pack()

    #later will check whether pacemaker is connected before displaying error message
    messagebox.showinfo(title="Connection Error",message="Pacemaker is not connected.")

    #check if new pacemaker is different than previous pacemaker
    # if pacemaker != current_pacemaker:
    #     messagebox.showinfo(title="New Pacemaker",message="New pacemaker device has been approached.")

    profile.mainloop()
