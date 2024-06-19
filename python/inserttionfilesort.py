from tkinter import *


from datetime import datetime
def insertionfilesort(root):

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
            test1 = 0



            for x in range (c):
                numofpass += 1

                if x >= (c/10) and test1 == 0:
                    print ("10%")
                    test1 += 1
                elif x >= ((2*c)/10) and test1 == 1:
                    print ("20%")
                    test1 += 1
                elif x >= ((c*3)/10) and test1 == 2:
                    print ("30%")
                    test1 += 1
                elif x >= ((c*4)/10) and test1 == 3:
                    print ("40%")
                    test1 += 1
                elif x >= ((c*5)/10) and test1 == 4:
                    print ("50%")
                    test1 += 1
                elif x >= ((c*6)/10) and test1 == 5:
                    print ("60%")
                    test1 += 1
                elif x >= ((c*7)/10) and test1 == 6:
                    print ("70%")
                    test1 += 1
                elif x >= ((c*8)/10) and test1 == 7:
                    print ("80%")
                    test1 += 1
                elif x >= ((c*9)/10) and test1 == 8:
                    print ("90%")
                    test1 += 1

                else:
                    ()


                for b in range (x):

                    if list[b] > list[x]:
                        data = list[b]
                        list[b] = list[x]
                        list[x] = data

        file.close
        file2 = open("neworderlist.txt","w")
        for x in range (c):

            file2.write(str(list[x])+"\n")
        print (list," it took",(numofpass)-1,"passes")
        end = datetime.now()

        print(f"Time taken in (hh:mm:ss.ms) is {end - start}")

        file2.close
    BSb1=Button(root,text="go",command=go)
    BSb1.pack()
    root.update()