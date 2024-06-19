from tkinter import *
file = open("alist.txt","w")
root = Tk()
Wtb = Entry(root)
Wtb.pack()
def writer():

    file.write( str(Wtb.get())+", \n")
Wb = Button(root,text = "write", command = writer)
Wb.pack()
root.mainloop()