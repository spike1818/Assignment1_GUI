class user:
    def __init__(person, username, password):
        person.username = username
        person.password = password

    def setUsername(person, u):
        person.username = u

    def getUsername(person):
        return person.username
    
    def setPassword(person, p):
        person.password = p

    def getPassword(person):
        return person.password
    
    def getUsers(person): #returns a list of lists containing usernames and passwords [(user1,pass1),(user2,pass2),etc...]
        users = []
        #open file
        file = open("loginInfo.txt", "r")
        data = file.readlines()
        for line in data:
            info_strip = line.strip("\n") #gets rid of the \n from all the items
            info = info_strip.split(" ") #splits items at spaces, seperating the usernames from the passwords
            singleUser = (info[0],info[1])
            users.append(singleUser) #adding each username and password
        file.close()
        #read users from file and store in users list
        return users