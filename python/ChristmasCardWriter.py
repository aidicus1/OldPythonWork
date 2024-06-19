from tkinter import *
import random

def ChristmasCardWriter(lewis):
    colour=("blue")
    colour2=("grey")

    CWtb = Entry(lewis,fg=colour2,bg=colour)
    CWtb2 = Entry(lewis,fg=colour2,bg=colour)
    CWtb.pack()
    CWtb2.pack()
    def CWcommand():
        CWfile = open("CCWmessages.txt","r")
        x = 0
        for line in CWfile:
            x += 1
        y = 0
        x=random.randint(1,x)
        CWfile = open("CCWmessages.txt","r")
        for line in CWfile:
            y += 1
            if y==x:
                CWline = line
        CWr = Tk()
        CWr.configure(bg=colour)
        CWl1 = Label(CWr ,text = "dear "+(CWtb.get()),fg=colour2,bg=colour).pack()
        CWl2 = Label(CWr ,text = (CWline),fg=colour2,bg=colour).pack()
        CWl3 = Label(CWr ,text = "from "+(CWtb2.get()),fg=colour2,bg=colour).pack()
        CWr.mainloop()
    CWb= Button(lewis,text ="go", command = CWcommand,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
    CWb.pack()

