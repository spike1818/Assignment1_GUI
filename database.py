from tkinter import *
import sqlite3
from tkinter import messagebox
import tkinter as tk
import welcome_screen

def changePassword(account_id, newPassword):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    accounts = query()

    for account in accounts:
        if (account[13] == account_id):
            username = account[0]
            password = newPassword
            firstName = account[2]
            lastName = account[3]
            lowerRateLimit = account[4]
            upperRateLimit = account[5]
            atrialAmplitude = account[6]
            atrialPulseWidth = account[7]
            ventricularAmplitude = account[8]
            ventricularPulseWidth = account[9]
            VRP_ = account[10]
            ARP_ = account[11]
            mode = account[12]

    c.execute("""UPDATE login_info SET
                username=:username,
                password=:password,
                firstName=:firstName,
                lastName=:lastName,
                lowerRateLimit=:lowerRateLimit,
                upperRateLimit=:upperRateLimit,
                atrialAmplitude=:atrialAmplitude,
                atrialPulseWidth=:atrialPulseWidth,
                ventricularAmplitude=:ventricularAmplitude,
                ventricularPulseWidth=:ventricularPulseWidth,
                VRP=:VRP,
                ARP=:ARP,
                mode=:mode

                WHERE oid = :oid""",

            {   'username':username,
                'password':newPassword,
                'firstName':firstName,
                'lastName':lastName,
                'lowerRateLimit':lowerRateLimit,
                'upperRateLimit':upperRateLimit,
                'atrialAmplitude':atrialAmplitude,
                'atrialPulseWidth':atrialPulseWidth,
                'ventricularAmplitude':ventricularAmplitude,
                'ventricularPulseWidth':ventricularPulseWidth,
                'VRP':VRP_,
                'ARP':ARP_,
                'mode':mode,
                'oid': account_id

        })
    #close connection
    conn.commit()
    conn.close()

def update(record_id):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    flag = True

    #name info
    if not(username_edit.get()):
        messagebox.showinfo(title="Invalid Username",message="Enter a valid username.")
    if len(username_edit.get()) < 4:
        messagebox.showinfo(title="Invalid Username",message="Username must be at least 4 characters.")
    if not(password_edit.get()):
        messagebox.showinfo(title="Invalid Password",message="Enter a valid password.")
    if len(password_edit.get()) < 8:
        messagebox.showinfo(title="Invalid Password",message="Password must be at least 8 characters.")
    if not(firstName_edit.get()):
        messagebox.showinfo(title="Invalid Name",message="Enter a valid first name.")
    if not(lastName_edit.get()):
        messagebox.showinfo(title="Invalid Name",message="Enter a valid last name.")


    if int(upperRateLimit_edit.get()) < int(lowerRateLimit_edit.get()):
        flag = False
        messagebox.showinfo(title="Rate Limit Error",message="Upper rate limit cannot be less than lower rate limit.")

    #lower rate limit
    if not(lowerRateLimit_edit.get().isdigit()): #make sure input is whole and non-negative
        flag = False
        messagebox.showinfo(title="Invalid Lower Rate Limit",message="Lower rate limit must be a non-negative whole number.")
    if (int(lowerRateLimit_edit.get()) < 30) or int(float(lowerRateLimit_edit.get())) > 175: #check if lower rate limit is within range
        flag = False
        messagebox.showinfo(title="Invalid Lower Rate Limit",message="Lower rate limit must be between 30-175ppm.")
    if 30 <= int(lowerRateLimit_edit.get()) <= 50: #check if correct incrementation for 30-50ppm
        if (int(lowerRateLimit_edit.get()) % 5) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 5ppm between 30-50ppm.")
    if 90 <= int(lowerRateLimit_edit.get()) <= 175: #check if correct incrementation for 90-175ppm
        if (int(lowerRateLimit_edit.get()) % 5) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 5ppm between 90-175ppm.")

    #upper rate limit
    if not(upperRateLimit_edit.get().isdigit()):
        messagebox.showinfo(title="Invalid Upper Rate Limit",message="Upper rate limit must be a non-negative whole number.")
    if (int(upperRateLimit_edit.get()) < 50) or (int(upperRateLimit_edit.get()) > 175): #check if upper rate limit is within range
        flag = False
        messagebox.showinfo(title="Invalid Upper Rate Limit",message="Upper rate limit must be between 50-175ppm.")
    if (50 < int(upperRateLimit_edit.get()) < 175):
        if (int(upperRateLimit_edit.get()) % 5) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 5ppm.")

    #atrial amplitude
    if not((atrialAmplitude_edit.get())[0].isdigit()):
        messagebox.showinfo(title="Invalid Atrial Amplitude",message="Atrial amplitude must be a non-negative decimal number.")
    if (float(atrialAmplitude_edit.get()) < 0) or (0 < float(atrialAmplitude_edit.get()) < 0.5) or (3.2 < float(atrialAmplitude_edit.get()) < 3.5) or (float(atrialAmplitude_edit.get()) > 7.0): #check if atrial amplitude is within range
        flag = False
        messagebox.showinfo(title="Invalid Atrial Amplitude",message="Atrial amplitude must be 0 or between 0.5-3.2V or 3.5-7.0V.")
    if (0.5 <= float(atrialAmplitude_edit.get()) <= 3.2): #check if correct incrementation for 0.5-3.2V
        if (int(100*float(atrialAmplitude_edit.get())) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.1V between 0.5-3.2V.")
    if (3.5 <= float(atrialAmplitude_edit.get()) <= 7.0): #check if correct incrementation for 3.5-7.0V
        if (int(100*float(atrialAmplitude_edit.get())) % 5) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.5V between 3.5-7.0V.")

    #atrial pulse width 
    if not(atrialPulseWidth_edit.get()[0].isdigit()):
        messagebox.showinfo(title="Invalid Atrial Pulse Width",message="Atrial pulse width must be a non-negative decimal number.")
    if (float(atrialPulseWidth_edit.get()) < 0.05) or ( 0.05 < float(atrialPulseWidth_edit.get()) < 0.1) or (float(atrialPulseWidth_edit.get()) > 1.9): #check if atrial pulse width is within range
        flag = False
        messagebox.showinfo(title="Invalid Atrial Pulse Width",message="Atrial pulse width must be equal to 0.05ms or between 0.1-1.9ms.")
    if (0.1 <= float(atrialPulseWidth_edit.get()) <= 1.9): #check if correct incrementation for 0.1-1.9ms
        if (int(100*float(atrialPulseWidth_edit.get())) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.1ms.")
    
    #ventricular amplitude
    if not(ventricularAmplitude_edit.get()[0].isdigit()):
        messagebox.showinfo(title="Invalid Ventricular Amplitude",message="Ventricular amplitude must be a non-negative decimal number.")
    if (float(ventricularAmplitude_edit.get()) < 0) or (0 < float(ventricularAmplitude_edit.get()) < 0.5) or (3.2 < float(ventricularAmplitude_edit.get()) < 3.5) or (float(ventricularAmplitude_edit.get()) > 7.0): #check if ventricular amplitude is within range
        flag = False
        messagebox.showinfo(title="Invalid Ventricular Amplitude",message="Ventricular amplitude must be 0 or between 0.5-3.2V or 3.5-7.0V.")
    if (0.5 <= float(ventricularAmplitude_edit.get()) <= 3.2): #check if correct incrementation for 0.5-3.2V
        if (int(100*float(ventricularAmplitude_edit.get())) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.1V between 0.5-3.2V.")
    if (3.5 <= float(ventricularAmplitude_edit.get()) <= 7.0): #check if correct incrementation for 3.5-7.0V
        if (int(100*float(ventricularAmplitude_edit.get())) % 50) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.5V between 3.5-7.0V.")

    # #ventricular pulse width
    if not(ventricularPulseWidth_edit.get()[0].isdigit()):
        messagebox.showinfo(title="Invalid Ventricular Pulse Width",message="Ventricular pulse width must be a non-negative decimal number.")
    if (float(ventricularPulseWidth_edit.get()) < 0.05) or (0.05 < float(ventricularPulseWidth_edit.get()) < 0.1) or (float(ventricularPulseWidth_edit.get()) > 1.9): #check if atrial pulse width is within range
        flag = False
        messagebox.showinfo(title="Invalid Ventricular Pulse Width",message="Ventricular pulse width must be equal to 0.05ms or between 0.1-1.9ms.")
    if (0.1 <= float(ventricularPulseWidth_edit.get()) <= 1.9): #check if correct incrementation for 0.1-1.9ms
        if (int(100*float(ventricularPulseWidth_edit.get())) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 0.1ms.")

    #VRP
    if not(VRP_edit.get().isdigit()): #make sure input is whole and non-negative
        flag = False
        messagebox.showinfo(title="Invalid VRP",message="Ventricular refractory period must be a non-negative whole number.")
    if (int(VRP_edit.get()) < 150) or (int(VRP_edit.get()) > 500):
        flag = False
        messagebox.showinfo(title="Invalid VRP",message="Ventricular refractory period must be between 150-500ms.")
    if (150 < int(VRP_edit.get()) < 500):
        if (int(VRP_edit.get()) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 10ms.")

    #ARP
    if not(ARP_edit.get().isdigit()): #make sure input is whole and non-negative
        flag = False
        messagebox.showinfo(title="Invalid ARP",message="Atrial refractory period must be a non-negative whole number.")
    if (int(ARP_edit.get()) < 150) or (int(ARP_edit.get()) > 500):
        flag = False
        messagebox.showinfo(title="Invalid ARP",message="Atrial refractory period must be between 150-500ms.")
    if (150 < int(ARP_edit.get()) < 500):
        if (int(ARP_edit.get()) % 10) != 0:
            flag = False
            messagebox.showinfo(title="Incrementation Error",message="Starting value must be incremented by 10ms.")

    #mode
    modes = ["AOO", "AAI", "VOO", "VVI", "OFF"]
    flag2 = False
    for mode in modes:
        if mode_edit.get() == mode:
            flag2 = True
    
    if flag2 == False:
        flag = False
        messagebox.showinfo(title="Invalid Mode",message="Enter one of the following modes: AOO, AAI, VOO, VVI, or OFF.")

    if flag == True:
        c.execute("""UPDATE login_info SET
                    username=:username,
                    password=:password,
                    firstName=:firstName,
                    lastName=:lastName,
                    lowerRateLimit=:lowerRateLimit,
                    upperRateLimit=:upperRateLimit,
                    atrialAmplitude=:atrialAmplitude,
                    atrialPulseWidth=:atrialPulseWidth,
                    ventricularAmplitude=:ventricularAmplitude,
                    ventricularPulseWidth=:ventricularPulseWidth,
                    VRP=:VRP,
                    ARP=:ARP,
                    mode=:mode

                    WHERE oid = :oid""",

                {   'username':username_edit.get(),
                    'password':password_edit.get(),
                    'firstName':firstName_edit.get(),
                    'lastName':lastName_edit.get(),
                    'lowerRateLimit':lowerRateLimit_edit.get(),
                    'upperRateLimit':upperRateLimit_edit.get(),
                    'atrialAmplitude':atrialAmplitude_edit.get(),
                    'atrialPulseWidth':atrialPulseWidth_edit.get(),
                    'ventricularAmplitude':ventricularAmplitude_edit.get(),
                    'ventricularPulseWidth':ventricularPulseWidth_edit.get(),
                    'VRP':VRP_edit.get(),
                    'ARP':ARP_edit.get(),
                    'mode':mode_edit.get(),
                    'oid': record_id

                })

        welcome_screen.login_name = str(firstName_edit.get() + " " + lastName_edit.get())
        welcome_screen.login_LRL = int(lowerRateLimit_edit.get())
        welcome_screen.login_URL = int(upperRateLimit_edit.get())
        welcome_screen.login_AA = float(atrialAmplitude_edit.get())
        welcome_screen.login_APW = float(atrialPulseWidth_edit.get())
        welcome_screen.login_VA = float(ventricularAmplitude_edit.get())
        welcome_screen.login_VPW = float(ventricularPulseWidth_edit.get())
        welcome_screen.login_VRP = int(VRP_edit.get())
        welcome_screen.login_ARP = int(ARP_edit.get())
        welcome_screen.login_M = str(mode_edit.get())
    
    #close connection
    conn.commit()
    conn.close()

#edit function
def edit(record_id):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    #query the database
    c.execute("SELECT * FROM login_info WHERE oid = " + record_id)
    records = c.fetchall() # list of lists for each row

    #global variables for text box names (this is needed to pass the contents of the box to the update function)
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
    editor.title("Edit Profile")
    editor.geometry("500x600")
    editor.configure(bg='#4863A0')

    editor_frame = tk.Frame(editor, bg='#4863A0')

    edit_data_label = Label(editor_frame, text="Edit Profile",bg='#4863A0', fg='#FFFFFF', font=("Arial", 24))

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
    ventricularAmplitude_edit_label = Label(editor_frame, text = "Ventricular Amplitude", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ventricularPulseWidth_edit_label = Label(editor_frame, text = "Ventricular Pulse Width", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    VRP_edit_label = Label(editor_frame, text = "VRP", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    ARP_edit_label = Label(editor_frame, text = "ARP", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
    mode_edit_label = Label(editor_frame, text = "Mode", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

    #save button
    save_btn = Button(editor_frame, text = "Save Changes", command= lambda: update(welcome_screen.login_id))
    back_btn = Button(editor_frame, text = "Back", command= editor.destroy)

    edit_data_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)

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
    back_btn.grid(row=15, column = 0, columnspan=2)


    #fill boxes with current info
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
        mode_edit.insert(0,record[12]) #the mode selected

    editor_frame.pack()
    editor.mainloop()
    #close connection
    conn.commit()
    conn.close() 

#delete function
def delete(idNum):

    #connect to database and create cursor
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    c.execute("DELETE from login_info WHERE oid =" + idNum)#use oid instead of username or password because there may be multiples

    conn.commit()
    conn.close()

#submit function
def submit(username, password, firstName, lastName,):

    #connect to database and create cursor
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    lowerRateLimit = 60
    upperRateLimit = 120
    atrialAmplitude = 3.5
    atrialPulseWidth = 0.4
    ventricularAmplitude = 3.5
    ventricularPulseWidth = 0.4
    VRP = 320
    ARP = 250
    mode = "OFF"

    #insert into table
    c.execute("INSERT INTO login_info VALUES(:username,:password,:firstName,:lastName,:lowerRateLimit,:upperRateLimit,:atrialAmplitude,:atrialPulseWidth,:ventricularAmplitude,:ventricularPulseWidth,:VRP,:ARP,:mode)",
            {
                'username':username,
                'password':password,
                'firstName':firstName,
                'lastName':lastName,
                'lowerRateLimit':lowerRateLimit,
                'upperRateLimit':upperRateLimit,
                'atrialAmplitude':atrialAmplitude,
                'atrialPulseWidth':atrialPulseWidth,
                'ventricularAmplitude':ventricularAmplitude,
                'ventricularPulseWidth':ventricularPulseWidth,
                'VRP':VRP,
                'ARP':ARP,
                'mode':mode
            })

    conn.commit()
    conn.close()

def query():

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    #query the database
    c.execute("SELECT *, oid FROM login_info")
    records = c.fetchall() # list of lists for each row

    conn.commit()
    conn.close()

    return records