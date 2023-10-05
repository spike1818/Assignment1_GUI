from tkinter import *
import sqlite3
from functools import partial
'''
root = Tk()
root.geometry("400x400")

#create database
conn = sqlite3.connect('login_list.db')

# Create cursor
c = conn.cursor()

#create table
#c.execute("CREATE TABLE login_info(username text, password text, first_name text, last_name text)")
'''

#delete function
def delete(username):

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()

    c.execute("DELETE from login_info WHERE username LIKE " + username)#use oid instead of username or password because there may be multiples

    #delete_box.delete(0,END)

    conn.commit()
    conn.close()



#submit function
def submit(username, password, firstName, lastName):

    #connect to database and create cursor (you need to do this inside the function as well, idk why)
    conn = sqlite3.connect('login_list.db')
    c = conn.cursor()
    print(username)
    print(password)
    #insert into table
    c.execute("INSERT INTO login_info VALUES(:user,:pword,:fname,:lname)",
            {
                'user':username,
                'pword':password,
                'fname':firstName,
                'lname':lastName
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
    
    # print_records = ''
    # for record in records:
    #     print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2])+  " " + str(record[3]) + " " + str(record[4]) + "\n"
    
    # query_label = Label(root, text = print_records)
    # query_label.grid(row = 10, column = 0, columnspan = 2)


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

delete_label = Label(root, text = "Delete ID")
delete_label.grid(row=7,column=0)

#submit button
submit_btn = Button(root, text="add login to database", command=lambda: submit(user.get(),pword.get(),fname.get(),lname.get()))
submit_btn.grid(row=5,column=0,columnspan=2,pady=10, padx=10)

#query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10)

#delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8,column=0,columnspan=2,pady=10, padx=10)

#commit changes
conn.commit()


#close connection
conn.close()

root.mainloop()
'''