import tkinter as tk
from tkinter import messagebox
import welcome_screen

def change_settings():
    settings = tk.Tk()
    settings.geometry("500x500")
    settings.configure(bg='#4863A0')
    settings.title("Settings Page")
    settings_topframe = tk.Frame(settings, bg='#4863A0')
    settings_middleframe = tk.Frame(settings, bg='#4863A0')
    settings_bottomframe = tk.Frame(settings, bg='#4863A0')


    #create info for corner of screen
    tracing_message = tk.Label(settings_topframe, text = "Settings", bg='#4863A0', fg='#FFFFFF', font=("Georgia", 20))
    back = tk.Button(settings_bottomframe, text = "Back to profile", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = settings.destroy)

    #entry boxes
    pulserate_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))
    pulsewidth_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))
    pulseamp_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))
    sensingsense_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))
    pacingmode_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))
    refracper_frequency_change = tk.Entry(settings_middleframe, font=("Arial", 12))

    #entry labels
    pulserate_title = tk.Label(settings_middleframe, text="Change Pulse Rate To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulsewidth_title = tk.Label(settings_middleframe, text="Change Pulse Width To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseamp_title = tk.Label(settings_middleframe, text="Change Pulse Amplitude To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    sensingsense_title = tk.Label(settings_middleframe, text="Change Sensing Sensitivity To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pacingmode_title = tk.Label(settings_middleframe, text="Change Pacing Mode To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    refracper_title = tk.Label(settings_middleframe, text="Change Refractory Period To: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

    #mode actuals
    pulserate_acc_title = tk.Label(settings_topframe, text="Pulse Rate: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulsewidth_acc_title = tk.Label(settings_topframe, text="Pulse Width: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pulseamp_acc_title = tk.Label(settings_topframe, text="Pulse Amplitude: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    sensingsense_acc_title = tk.Label(settings_topframe, text="Sensing Sensitivity: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    pacingmode_acc_title = tk.Label(settings_topframe, text="Pacing Mode: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    refracper_acc_title = tk.Label(settings_topframe, text="Refractory Period: ", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

    tracing_message.grid(row=0, column=0, pady=10)
    back.grid(row=0, column=0)
    #mode change alignment
    pulserate_frequency_change.grid(row=0,column=1)
    pulsewidth_frequency_change.grid(row=1,column=1)
    pulseamp_frequency_change.grid(row=2,column=1)
    sensingsense_frequency_change.grid(row=3,column=1)
    pacingmode_frequency_change.grid(row=4,column=1)
    refracper_frequency_change.grid(row=5,column=1)

    #change labels alignment
    pulserate_title.grid(row=0,column=0)
    pulsewidth_title.grid(row=1,column=0)
    pulseamp_title.grid(row=2,column=0)
    sensingsense_title.grid(row=3,column=0)
    pacingmode_title.grid(row=4,column=0)
    refracper_title.grid(row=5,column=0)

    #acc title alignment
    pulserate_acc_title.grid(row=2,column=0)
    pulsewidth_acc_title.grid(row=3,column=0)
    pulseamp_acc_title.grid(row=4,column=0)
    sensingsense_acc_title.grid(row=5,column=0)
    pacingmode_acc_title.grid(row=6,column=0)
    refracper_acc_title.grid(row=7,column=0)

    settings_middleframe.grid_rowconfigure(9, minsize=50)
    settings_middleframe.grid_rowconfigure(1, minsize=20)
    settings_topframe.grid_rowconfigure(9, minsize=40)
    settings_topframe.pack()
    settings_middleframe.pack()
    settings_bottomframe.pack()

    #later will check whether pacemaker is connected before displaying error message

    settings.mainloop()
