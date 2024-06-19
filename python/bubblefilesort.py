from tkinter import *
from datetime import datetime
def bubblefilesort(root):
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

        numofpass = 0
        y = 1
        c =len(list)
        while y == 1:
            y = 0


            for x in range (c-1):


                if list[x] > list[x+1]:
                    data = list[x+1]
                    list[x+1] = list[x]
                    list[x] = data
                    y = 1
                numofpass += 1
        file.close
        file2 = open("orderlist.txt","w")
        for x in range (c):

            file2.write(str(list[x])+"\n")
        print (list," it took",numofpass,"passes")
        end = datetime.now()

        print(f"Time taken in (hh:mm:ss.ms) is {end - start}")
        file2.close
    BSb1=Button(root,text="go",command=go)
    BSb1.pack()
    root.update()
