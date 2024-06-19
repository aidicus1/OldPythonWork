from tkinter import *

from datetime import datetime
def Linearsearch(root):
    BStb1 = Entry(root)
    BStb1.pack()
    BStb2 = Entry(root)
    BStb2.pack()
    def go ():
        searchedfor = int(BStb2.get())
        start = datetime.now()
        fileinput = (BStb1.get()+".txt")
        file = open(fileinput,"r")
        list = []
        for line in file:
            data = line.split(",")
            list.append(int(data[0]))
        numofpass = 0
        y = 1
        c =len(list)
        found = True
        while y == 1:
            y = 0
            for x in range (c):
                if list[x] == searchedfor:
                    print ("located at line ",x)
                    found = False
                else:
                    ()
            if found == False:
                ()
            else:
                print ("not in file")
        end = datetime.now()
        time = (f"Time taken in (hh:mm:ss.ms) is {end - start}")
        LSl1.configure(text = time)
        root.update
    BSb1=Button(root,text="go",command=go)
    BSb1.pack()
    LSl1 = Label(root,text="will display time")
    LSl1.pack()
    root.update()