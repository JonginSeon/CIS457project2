import os
from tkinter import *
from ftplib import FTP

root = Tk()
root.title("Project 2")

client = FTP()

#   This is the function used to register a user
#   The centralized server connects to the user's server
#   and retrives the file containing the necessary information
#   This function is executed when the user clicks 
#   connect from the GUI
def registerUser():
    #acquiring all information input by the user
    serverHostname = serverHostnameEntry.get()
    port = int (portEntry.get())
    username = usernameEntry.get()
    hostname = hostnameEntry.get()
    speed = speedEntry.get()
    keyword = searchEntry.get()


    #connecting to the host's server 
    #and retrieving the required file
    client.connect(serverHostname,port)
    client.login("user", "pass")
    file = open( "descriptions.txt", "ab")
    client.retrbinary("RETR " + "descriptions.txt", file.write)    
    file.close()

    #adding a new line to the file after retrieving from each host
    fo = open("descriptions.txt","a+")
    fo.write("\n")
    fo.close()
    text.insert(END,"Received descriptions.txt file from " + username + "\n")
    client.close()
    


#   This is the function used to search for a keyword
#   The centralized server searches the file information it
#   received from all hosts for the input keyword
#   This function is executed when the user clicks
#   search from the GUI
def findKeyWord():
    keyword = searchEntry.get()
    with open("descriptions.txt","r") as openfile:
        for line in openfile:
            for part in line.split():
                if keyword in part:
                    #print the line to the text widget of the GUI
                    text.insert(END,(line + "\n"))	

        

# tkinter label widgets for the GUI
serverHostnameLabel = Label(root, text="Server Hostname")
portLabel = Label(root, text="Port")
usernameLabel = Label(root, text="Username")
hostnameLabel = Label(root, text="Hostname")
speedLabel = Label(root, text="Speed")
searchLabel = Label(root, text="Search")

# tkinter button widgets for GUI
connectBtn = Button(root, text="Connect", command = registerUser)
searchBtn = Button(root, text="Search", command = findKeyWord)

# tkinter entry widgets for the GUI
serverHostnameEntry = Entry(root)
portEntry = Entry(root)
usernameEntry = Entry(root)
hostnameEntry = Entry(root)
speedEntry = Entry(root)
searchEntry = Entry(root)

# placing the widgets on the GUI using the grid
serverHostnameLabel.grid(row=0, sticky=E)
portLabel.grid(row=0, column=3, sticky=E)
usernameLabel.grid(row=1, sticky=E)
hostnameLabel.grid(row=1, column=3, sticky=E)
speedLabel.grid(row=1, column=5, sticky=E)
searchLabel.grid(row=2, sticky=E)


serverHostnameEntry.grid(row=0, column=1)
portEntry.grid(row=0, column=4)
usernameEntry.grid(row=1, column=1)
hostnameEntry.grid(row=1, column=4)
speedEntry.grid(row=1, column=6)
searchEntry.grid(row=2, column=1)


connectBtn.grid(row=0,column=6)
searchBtn.grid(row=2, column=4)

# tkinter text widget for the GUI
text = Text(root, borderwidth=3, relief="sunken")
text.config(font=("consolas", 12), undo=True, wrap='word')
text.grid(row=4, column=1, sticky="nsew")

root.mainloop()


