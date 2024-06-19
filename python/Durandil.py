import random
import os
from tkinter import *
root = Tk()
def error():
    error = Tk()
    El = Label(error,text="error")
    El.pack()
    error.mainloop()
def durandil(root):
    Dtb1 = Entry(root)
    Dtb2 = Entry(root)
    Dtb3 = Entry(root)
    Df1 = open("converter2.txt","r")
    Dpl = random.randint(8,12)
    Dp = []
    for x in range(Dpl):
        Dp.append("¬")
    Dlc = random.randint(1,(Dpl-1))
    Dg1 = 1
    while Dg1 == 1:
        Duc = random.randint(1,(Dpl-1))
        if Duc == Dlc:
            ()
        else:
            Dg1 = 0
    Dg1 = 1
    while Dg1 == 1:
        Dsc = random.randint(1,(Dpl-1))
        if Dsc == Dlc or Dsc == Duc:
            ()
        else:
            Dg1 = 0
    Duc2 = random.randint(27,52)
    Dlc2 = random.randint(1,26)
    Dsc2 = random.randint(53,95)
    for line in Df1:
        data = line.split("¬")
        if data[1] == str(Duc2):

            Duc2 = data[0]
        elif data[1] == str(Dlc2):
            Dlc2 = data[0]
        elif data[1] == str(Dsc2):
            Dsc2 = data[0]
        else:
            ()
    Df1.close()
    Dp[Duc]=Duc2
    Dp[Dlc]=Dlc2
    Dp[Dsc]=Dsc2
    Df2 = open("temp.txt","w")
    for x in range(len(Dp)):
        if Dp[x] == "¬":
            Dc = random.randint(1,95)
            Df1=open("converter2.txt","r")
            for line in Df1:
                data= line.split("¬")
                if data[1] == str(Dc):
                    Dp[x] = data[0]
                else:
                    ()
            Df1.close()
        Df2.write(Dp[x])
    Df2.close()
    Df2 = open("temp.txt","r")
    for line in Df2:
        Dp = (line)
    Df2.close()
    os.remove("temp.txt")
    Dtb1.pack()
    Dtb2.pack()
    Dtb3.pack()
    Dtb2.insert(0,Dp)
    def Dca():
        Df5 = open("newdetails.txt","r")
        Df6 = open("temp2.txt","w")
        for line in Df5:
            data=line.split(",")
            Df6.write(data[0]+"¬\n")
        Df5.close()
        Df6.close()
        Df6 = open("temp2.txt","r")
        infile = "0"
        for line in Df6:
            data = line.split("¬")
            if data[0] == str(Dtb1.get()):
                infile = "1"
        Df6.close()
        if Dtb2.get()==Dtb3.get() and str(Dtb1.get()) != " " and infile=="0":
            Dp3 = "¬".join(Dtb2.get())
            Dp3 =Dp3.split("¬")
            Dh1 = 0
            Dh2 = 0
            Dh3 = 0
            for x in range (len(Dp3)):
                Df7 = open("converter2.txt","r")
                for line in Df7:
                    data2 = line.split("¬")
                    if data2[0] == str(Dp3[x]):
                        if int(data2[1]) <= 26:
                            Dh1 = 1
                        elif int(data2[1]) > 26 and int(data2[1]) <= 52:
                            Dh2 = 1
                        elif int(data2[1]) > 52:
                            Dh3 = 1
                        else:
                            error()
                Df7.close()
            if Dh1 == 1 and Dh2 == 1 and Dh3 ==1 and len(Dp3) >= 8:
                from Encrypter import caliburn
                caliburn(Dp)
                Df3 = open("temp.txt","r")
                for line in Df3:
                    Dp2 =(line)
                Df3.close()
                os.remove("temp.txt")
                Df4 = open("newdetails.txt","a")
                Df4.write(str(Dtb1.get())+","+str(Dp2)+",\n")
                Df4.close()
            else:
                ()
        else:
            ()
        os.remove("temp2.txt")
    Db1 = Button(root,text="create account",command=Dca)
    Db1.pack()
    root.mainloop()
durandil(root)



