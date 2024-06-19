from tkinter import *

from datetime import datetime
def mean(root):
    BStb1 = Entry(root)
    BStb1.pack()


    def go ():
        start = datetime.now()
        fileinput = (BStb1.get()+".txt")
        file = open(fileinput,"r")
        list = []
        for line in file:
            data = line.split(",")
            list.append(int(data[0]))
        print ((sum(list)/len(list)))
    BSb1=Button(root,text="go",command=go)
    BSb1.pack()
    root.update