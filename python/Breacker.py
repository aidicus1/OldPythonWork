from tkinter import *
import random

def breaker(lewis):
    CWfile = open("CCWmessages.txt","r")
    file = open("year12.txt","r")
    x = 0
    for line in CWfile:
        x += 1
    y = 0
    x=random.randint(0,x)
    file = open("CCWmessages.txt","r")
    for line in file:
        y += 1
        if y==x:
            CWline = line
    CWtb = Entry(lewis)
    CWtb2 = Entry(lewis)
    CWtb.pack()
    CWtb2.pack()
    def CWcommand():
        CWr = Tk()
        CWl1 = Label(CWr ,text = (CWtb.get())).pack()
        CWl2 = Label(CWr ,text = (CWline)).pack()
        CWl3 = Label(CWr ,text = (CWtb2.get())).pack()
        CWr.mainloop()
    CWb= Button(lewis,text ="go", command = CWcommand)
    CWb.pack()

