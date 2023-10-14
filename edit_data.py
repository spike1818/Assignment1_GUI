import tkinter as tk
from tkinter import *
import database
import welcome_screen

def edit_data():
    global username_edit
    global password_edit
    global firstName_edit
    global lastName_edit
    global lowerRateLimit_edit
    global upperRateLimit_edit
    global atrialAmplitude_edit
    global atrialPulseWidth_edit
    global ventricularAmplitude_edit
    global ventricularPulseWidth_edit
    global VRP_edit
    global ARP_edit
    global mode_edit

    editor = Tk()
    editor.title('Edit Data')
    editor.geometry("500x600")
    editor.configure(bg='#4863A0')

    editor_frame = tk.Frame(editor, bg='#4863A0')

    edit_data_label = Label(editor_frame, text="Edit Settings",bg='#4863A0', fg='#FFFFFF', font=("Arial", 24))

    #input field
    username_edit = Entry(editor_frame, font=("Arial",12))
    password_edit = Entry(editor_frame, font=("Arial", 12))
    firstName_edit = Entry(editor_frame, font=("Arial", 12))
    lastName_edit = Entry(editor_frame, font=("Arial", 12))
    lowerRateLimit_edit = Spinbox(editor_frame, from_= 30, to= 175, increment = 5, font=("Arial", 12))#needs to be increment 1 for 50-90
    upperRateLimit_edit = Spinbox(editor_frame, from_= 50, to= 175, increment = 5, font=("Arial", 12))
    atrialAmplitude_edit = Spinbox(editor_frame, from_= 0.5, to= 7.0, increment = 0.1, font=("Arial", 12))#needs to be increment 0.5 for 3.5-7
    atrialPulseWidth_edit = Spinbox(editor_frame, from_= 0.1, to= 1.9, increment = 0.1, font=("Arial", 12))#single step from 0.1 - 0.05
    ventricularAmplitude_edit = Spinbox(editor_frame, from_= 0.5, to= 7.0, increment = 0.1, font=("Arial", 12))#same as atrialAmplidtude
    ventricularPulseWidth_edit = Spinbox(editor_frame, from_= 0.1, to= 1.9, increment = 0.1, font=("Arial", 12))#same as atrial
    VRP_edit = Spinbox(editor_frame, from_= 150, to= 500, increment = 10, font=("Arial", 12))
    ARP_edit = Spinbox(editor_frame, from_= 150, to= 500, increment = 10, font=("Arial", 12))
    mode_edit = Entry(editor_frame, font=("Arial", 12))#this can be a drop down menu, if not we can keep it as a text input

    #input labels
    username_edit_label = Label(editor_frame, text = "Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    password_edit_label = Label(editor_frame, text = "Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    firstName_edit_label = Label(editor_frame, text = "First Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    lastName_edit_label = Label(editor_frame, text = "Last Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    lowerRateLimit_edit_label = Label(editor_frame, text = "Lower Rate Limit", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    upperRateLimit_edit_label = Label(editor_frame, text = "Upper Rate Limit", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    atrialAmplitude_edit_label = Label(editor_frame, text = "Atrial Amplitude", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    atrialPulseWidth_edit_label = Label(editor_frame, text = "Atrial Pulse Width", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ventricularAmplitude_edit_label = Label(editor_frame, text = "Vetricular Amplitude", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ventricularPulseWidth_edit_label = Label(editor_frame, text = "Ventricular Pulse Width", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    VRP_edit_label = Label(editor_frame, text = "VRP", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ARP_edit_label = Label(editor_frame, text = "ARP", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    mode_edit_label = Label(editor_frame, text = "Mode", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

    #save button
    save_btn = Button(editor_frame, text = "Save Changes", command= lambda: database.update(welcome_screen.login_id))

    edit_data_label.grid(row=0, column=0, columnspan=2, pady=10)

    #place input boxes
    username_edit.grid(row=1, column = 1, padx=20, pady=10)
    password_edit.grid(row=2, column = 1)
    firstName_edit.grid(row=3, column = 1, pady=10)
    lastName_edit.grid(row=4, column = 1)
    lowerRateLimit_edit.grid(row=5, column = 1, pady=10)
    upperRateLimit_edit.grid(row=6, column = 1)
    atrialAmplitude_edit.grid(row=7, column = 1, pady=10)
    atrialPulseWidth_edit.grid(row=8, column = 1)
    ventricularAmplitude_edit.grid(row=9, column = 1, pady=10)
    ventricularPulseWidth_edit.grid(row=10, column = 1)
    VRP_edit.grid(row=11, column = 1, pady=10)
    ARP_edit.grid(row=12, column = 1)
    mode_edit.grid(row=13, column = 1, pady=10)
    
    #place input labels
    username_edit_label.grid(row=1,column = 0)
    password_edit_label.grid(row=2,column = 0)
    firstName_edit_label.grid(row=3,column = 0)
    lastName_edit_label.grid(row=4,column = 0)
    lowerRateLimit_edit_label.grid(row=5,column = 0)
    upperRateLimit_edit_label.grid(row=6,column = 0)
    atrialAmplitude_edit_label.grid(row=7,column = 0)
    atrialPulseWidth_edit_label.grid(row=8,column = 0)
    ventricularAmplitude_edit_label.grid(row=9,column = 0)
    ventricularPulseWidth_edit_label.grid(row=10,column = 0)
    VRP_edit_label.grid(row=11,column = 0)
    ARP_edit_label.grid(row=12,column = 0)
    mode_edit_label.grid(row=13,column = 0)

    #place save button
    save_btn.grid(row=14, column = 0, columnspan=2, pady=10)

    #fill boxes with current info
    records = database.query()
    for record in records:
        username_edit.insert(0,record[0])
        password_edit.insert(0,record[1])
        firstName_edit.insert(0,record[2])
        lastName_edit.insert(0,record[3])
        lowerRateLimit_edit.delete(0,"end") #spinboxes will automatically fill with lowest value, this is needed to clear them before putting the acutal value in there
        lowerRateLimit_edit.insert(0,record[4])
        upperRateLimit_edit.delete(0,"end")
        upperRateLimit_edit.insert(0,record[5])
        atrialAmplitude_edit.delete(0,"end")
        atrialAmplitude_edit.insert(0,record[6])
        atrialPulseWidth_edit.delete(0,"end")
        atrialPulseWidth_edit.insert(0,record[7])
        ventricularAmplitude_edit.delete(0,"end")
        ventricularAmplitude_edit.insert(0,record[8])
        ventricularPulseWidth_edit.delete(0,"end")
        ventricularPulseWidth_edit.insert(0,record[9])
        VRP_edit.delete(0,"end")
        VRP_edit.insert(0,record[10])
        ARP_edit.delete(0,"end")
        ARP_edit.insert(0,record[11])
        mode_edit.insert(0,record[12])

    editor_frame.pack()
    editor.mainloop()