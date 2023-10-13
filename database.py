from tkinter import *
import sqlite3
from functools import partial
'''
root = Tk()
root.geometry("400x400")
'''
#create database
conn = sqlite3.connect('login_list.db')

# Create cursor
c = conn.cursor()

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

def update(record_id):

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    c.execute("""UPDATE login_info SET
        username = :user,
        password = :pword,
        first_name = :first,
        last_name = :last

        WHERE oid = :oid""",
        {'user': user_edit.get(),
        'pword': pword_edit.get(),
        'first': fname_edit.get(),
        'last': lname_edit.get(),
        'oid': record_id

        })

    #close connection
    conn.commit()
    conn.close()

#edit function
def edit(record_id):
    editor = Tk()
    editor.title('Update')
    editor.geometry("400x600")

    #open connection
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    #query the database
    c.execute("SELECT * FROM login_info WHERE oid = " + record_id)
    records = c.fetchall() # list of lists for each row

    #global variables for text box names
    global user_edit
    global pword_edit
    global fname_edit
    global lname_edit

    #text boxes for test input
    user_edit = Entry(editor, width = 30)
    user_edit.grid(row=0, column = 1, padx=20)
    pword_edit = Entry(editor, width = 30)
    pword_edit.grid(row=1, column = 1)
    fname_edit = Entry(editor, width = 30)
    fname_edit.grid(row=2, column = 1)
    lname_edit = Entry(editor, width = 30)
    lname_edit.grid(row=3, column = 1)

    #labels
    user_edit_label = Label(editor, text = "Username")
    user_edit_label.grid(row=0,column = 0)
    pword_edit_label = Label(editor, text = "Password")
    pword_edit_label.grid(row=1,column = 0)
    fname_edit_label = Label(editor, text = "First Name")
    fname_edit_label.grid(row=2,column = 0)
    lname_edit_label = Label(editor, text = "Last Name")
    lname_edit_label.grid(row=3,column = 0)

    #fill boxes with current info
    for record in records:
        user_edit.insert(0,record[0])
        pword_edit.insert(0,record[1])
        fname_edit.insert(0,record[2])
        lname_edit.insert(0,record[3])

    #save button
    save_btn = Button(editor, text = "Save Changes", command= lambda: update(record_id))
    save_btn.grid(row=4, column = 0)

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