import random
from tkinter import *
root =Tk()
BStb1 = Entry(root)
BStb1.pack()
list = []

def go():
    for x in range (int(BStb1.get())):
        data = random.randint(1,100)
        list.append(data)
    print(list)

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

BSb1=Button(root,text="go",command=go)
BSb1.pack()
root.mainloop()



