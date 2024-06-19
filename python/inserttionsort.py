from tkinter import *
root = Tk()
import random
from datetime import datetime
def insertionfilesort(root):
    fStb1 = Entry(root)
    fStb1.pack()
    BStb2 = Entry(root)
    BStb2.pack()
    fStb1.insert(0,"100")
    BStb2.insert(0,"100")
    list = []
    def go ():
        start = datetime.now()
        for x in range (int(fStb1.get())):
            data = random.randint(1,int(BStb2.get()))
            list.append(data)


        numofpass = 0
        y = 1
        c =len(list)
        while y == 1:
            y = 0


            for x in range (c):
                numofpass += 1

                for b in range (x):

                    if list[b] > list[x]:
                        data = list[b]
                        list[b] = list[x]
                        list[x] = data
        file2 = open("anotherneworderlist.txt","w")
        for x in range (c):

            file2.write(str(list[x])+"\n")
        print (list," it took",(numofpass)-1,"passes")
        end = datetime.now()

        print(f"Time taken in (hh:mm:ss.ms) is {end - start}")
        file2.close
    BSb1=Button(root,text="go",command=go)
    BSb1.pack()
    root.mainloop()
insertionfilesort(root)