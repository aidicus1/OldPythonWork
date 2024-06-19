import random
from tkinter import *
root = Tk()
from datetime import datetime
def bubblesort(shay):
    BStb1 = Entry(shay)
    BStb1.pack()
    BStb2 = Entry(shay)
    BStb2.pack()
    BStb2.insert(0,"100")
    BStb1.insert(0,"100")
    list = []

    def go():
        start = datetime.now()
        for x in range (int(BStb1.get())):
            data = random.randint(1,int(BStb2.get()))
            list.append(data)


        numofpass = 0
        y = 1
        while y == 1:
            y = 0
            numofpass += 1



            for x in range (len(list)-1):

                if list[x] > list[x+1]:
                    data = list[x+1]
                    list[x+1] = list[x]
                    list[x] = data
                    y = 1
        print (list," it took",numofpass,"passes")
        end = datetime.now()

        print(f"Time taken in (hh:mm:ss.ms) is {end - start}")

    BSb1=Button(shay,text="go",command=go)
    BSb1.pack()
    shay.mainloop()
bubblesort(root)


