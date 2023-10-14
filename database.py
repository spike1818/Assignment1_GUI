from tkinter import *
import sqlite3
from edit_data import *

'''
root = Tk()
root.geometry("400x400")

#create database
conn = sqlite3.connect('login_list.db')

# Create cursor
c = conn.cursor()
'''
#create table
'''
c.execute("""CREATE TABLE login_info(
            username text, 
            password text, 
            firstName text, 
            lastName text, 
            lowerRateLimit integer,
            upperRateLimit integer,
            atrialAmplitude real,
            atrialPulseWidth real,
            ventricularAmplitude real,
            ventricularPulseWidth real,
            VRP integer,
            ARP integer,
            Mode text
          )""")
'''

def changePassword(account_id, newPassword):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    accounts = query()

    username
    password
    firstName
    lastName
    lowerRateLimit
    upperRateLimit
    atrialAmplitude
    atrialPulseWidth
    ventricularAmplitude
    ventricularPulseWidth
    VRP
    ARP
    mode

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
            VRP = account[10]
            ARP = account[11]
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
                'mode':mode,
                'oid': account_id

        })

def update(record_id):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

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
        
    # clicked = StringVar()
    # clicked.set("AOO")
    # mode_edit = OptionMenu(editor_frame, clicked, "AOO", "AAI", "VOO", "VVI")

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
    save_btn = Button(editor_frame, text = "Save Changes", command= lambda: update(welcome_screen.login_id))

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

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    c.execute("DELETE from login_info WHERE oid =" + idNum)#use oid instead of username or password because there may be multiples

    #delete_box.delete(0,END)

    conn.commit()
    conn.close()



#submit function
def submit(username, password, firstName, lastName,):

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()
    print(username)
    print(password)

    lowerRateLimit = 60
    upperRateLimit = 120
    atrialAmplitude = 3.5
    atrialPulseWidth = 0.4
    ventricularAmplitude = 3.5
    ventricularPulseWidth = 0.4
    VRP = 320
    ARP = 250
    mode = "off"

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

    #clear text boxes
    #user.delete(0, END)
    #pword.delete(0, END)
    #fname.delete(0, END)
    #lname.delete(0, END)



def query():

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    #query the database
    c.execute("SELECT *, oid FROM login_info")
    records = c.fetchall() # list of lists for each row
    print(records)
    '''
    print_records = ''
    for record in records:
         print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2])+  " " + str(record[3]) + " " + str(record[4]) + "\n"
    
    query_label = Label(root, text = print_records)
    query_label.grid(row = 10, column = 0, columnspan = 2)
    '''

    conn.commit()
    conn.close()

    return records


'''
#text boxes for test input
user = Entry(root, width = 30)
user.grid(row=0, column = 1, padx=20)

pword = Entry(root, width = 30)
pword.grid(row=1, column = 1)

fname = Entry(root, width = 30)
fname.grid(row=2, column = 1)

lname = Entry(root, width = 30)
lname.grid(row=3, column = 1)

delete_box = Entry(root, width = 30)
delete_box.grid(row=7, column = 1)

#labels
user_label = Label(root, text = "Username")
user_label.grid(row=0,column = 0)

pword_label = Label(root, text = "Password")
pword_label.grid(row=1,column = 0)

fname_label = Label(root, text = "First Name")
fname_label.grid(row=2,column = 0)

lname_label = Label(root, text = "Last Name")
lname_label.grid(row=3,column = 0)

delete_label = Label(root, text = "Select ID")
delete_label.grid(row=7,column=0)

#submit button
submit_btn = Button(root, text="add login to database", command=lambda: submit(user.get(),pword.get(),fname.get(),lname.get()))
submit_btn.grid(row=5,column=0,columnspan=2,pady=10, padx=10)

#query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10)


#select button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8,column=0,columnspan=2,pady=10, padx=10)

#edit button
edit_btn = Button(root, text="Edit Record", command=lambda: edit(delete_box.get()))
edit_btn.grid(row=9,column=0,columnspan=2,pady=10, padx=10)

#commit changes
conn.commit()


#close connection
conn.close()

root.mainloop()
'''