from tkinter import *
import os
import time
root = Tk()
colour=("blue")
colour2=("grey")
img = PhotoImage(file='ATindustriesLogo.png')
labelImg = Label(image=img,bg=colour)
labelImg.place(x=370)
root.configure(background=colour)
root.title("ASCALON (copywrite ATindustries do not distribute)")
root.geometry('445x130')
def Ago():
    username = Atb1.get()
    password = Atb2.get()
    if username != "":
        file5 = open("details.txt","r")
        from Encrypter import encrypter
        encrypter(password)
        file56 = open("temp.txt","r")
        for line in file56:
            newpassword = line
        file56.close()
        os.remove("temp.txt")
        for line in file5:
            data = line.split(",")
            if username  == data[0] and newpassword == data[1]:
                file6 = open("systemlog.txt","a")
                localtime = time.asctime( time.localtime(time.time()) )
                file6.write(username+" started "+localtime+"\n")
                splited = ','.join(password)
                splited= splited.split(",")
                file = open("converter2.txt","r")
                for line in file:
                    data=line.split("¬")
                    for x in range(len(splited)):
                        if splited[x] == data[0]:
                            splited[x] = int(data[1])
                        else:
                            ()
                key1 = splited[0]
                key3 = splited[0]
                key4 = splited[0]
                for x in range (len(splited)):
                    key1 += splited[x]
                    key3 *= (splited[x] + splited[x])
                    key4 *= splited[x]
                file.close()
                Gfile= open(str(Atb1.get())+"list.txt","r")
                Gfile2 = open(str(Atb1.get())+"dictionary.txt","r")
                for line in Gfile:
                    Glist=line.split(" ")
                Glist3 = []
                for line in Gfile2:
                    Glist2 = line.split(",")
                    for x in range(len(Glist2)):
                        for y in range(len(Glist)-1):
                            Glist4 = Glist[y].split(",")
                            if Glist2[x] ==Glist4[1]:
                                if Glist4[0] == "/n":
                                    Glist3.append("\n")
                                else:
                                    Glist3.append(Glist4[0])
                Gfile.close()
                newlist = Glist3
                for y in range (len(Glist3)):
                    if newlist[y] != "\n" and newlist[y] != "":
                        newlist[y]= int((((int(Glist3[y])-key4)/key4)-key1)/key3)
                        file4 = open("converter2.txt","r")
                        for line2 in file4:
                            data = line2.split("¬")
                            if str(newlist[y]) == str(data[1]):
                                newlist[y] = data[0]
                            else:
                                ()
                    else:
                        ()
                Afile = open("newtemp.txt","w")
                for x in range (len(newlist)):
                    Afile.write(newlist[x])
                Afile.close()
                Afile = open("newtemp.txt","r")
                for line in Afile:
                    Alist = line
                Afile.close()
                os.remove("newtemp.txt")
                Alistdata = Alist.split("~")
                Atb1.destroy()
                Atb2.destroy()
                Ab1.destroy()
                Al2.destroy()
                Al3.destroy()
                def Ago3():
                    def Aend():
                        localtime = time.asctime( time.localtime(time.time()) )
                        file6.write(username+" ended "+localtime+"\n")
                        file6.close()
                        root.destroy()
                    Al4 = Label(root,text = str(Alistdata[0]),bg=colour,fg=colour2)
                    Al2 = Label(root,text = str(Alistdata[1]),bg=colour,fg=colour2)
                    Al3 = Label(root,text = str(Alistdata[2]),bg=colour,fg=colour2)
                    Al4.place(x=160,y=25)
                    Al2.place(x=160,y=50)
                    Al3.place(x=160,y=75)
                    def rewrite():
                        Ab2.destroy()
                        def Ago2():
                            Alist2 = []
                            Alistdata[0]=(Atb3.get())
                            Alistdata[1]=(Atb4.get())
                            Alistdata[2]=(Atb5.get())
                            for x in range ((len(Alistdata))-1):
                                Asplited=[]
                                Asplited = "¬".join(Alistdata[x])
                                Asplited = Asplited.split("¬")
                                if Asplited != "~":
                                    Asplited.append("~")
                                else:
                                    ()
                                for y in range (len(Asplited)):
                                    Afile2 = open("converter2.txt","r")
                                    for line in Afile2:
                                        data=line.split("¬")
                                        if data[0] == Asplited[y]:
                                            Alist2.append(int(data[1]))
                                        else:
                                            ()
                                    Afile2.close()
                            Alist3 = []
                            Adictionary = []
                            Afile3 = open(username+"list.txt","w")
                            Afile4 = open(username+"dictionary.txt","w")
                            count = 1
                            for x in range (len(Alist2)):
                                Alist2[x] = (str(key4*((key3*Alist2[x])+key1)+key4))
                                inlist = 0
                                for y in range (len(Alist3)):
                                    count += 1
                                    Alist3data = Alist3[y].split(",")
                                    if str(Alist3data[0]) == Alist2[x]:
                                        Adictionary.append(Alist3data[1])
                                        Afile4.write(str(Alist3data[1])+",")
                                        inlist = 1
                                    else:
                                        ()
                                if inlist != 1:
                                    Adictionary.append(count)
                                    Alist3.append(Alist2[x]+","+str(count))
                                    Afile4.write(str(count)+",")
                                    Afile3.write(str(Alist2[x]+","+str(count)+" "))
                                else:
                                    ()
                            Atb3.destroy()
                            Atb4.destroy()
                            Atb5.destroy()
                            Ab4.destroy()
                            Ab3.destroy()
                            Ago3()
                        Al4.destroy()
                        Al2.destroy()
                        Al3.destroy()
                        Atb3 = Entry(root,bg=colour2,fg=colour)
                        Atb3.place(x=160,y=25)
                        Atb3.insert(0,str(Alistdata[0]))
                        Atb4 = Entry(root,bg=colour2,fg=colour)
                        Atb4.place(x=160,y=50)
                        Atb4.insert(0,str(Alistdata[1]))
                        Atb5= Entry(root,bg=colour2,fg=colour)
                        Atb5.place(x=160,y=75)
                        Atb5.insert(0,str(Alistdata[2]))
                        Ab3= Button(root,command = Ago2, text = "Update",bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
                        Ab3.place(x=140,y=100)
                    Al5= Label(root,text="Note 1",bg=colour,fg=colour2)
                    Al6=Label(root,text="Note 2",bg=colour,fg=colour2)
                    Al7=Label(root,text="Note 3",bg=colour,fg=colour2)
                    Al5.place(x=100,y=25)
                    Al6.place(x=100,y=50)
                    Al7.place(x=100,y=75)
                    Ab2 = Button(root,command = rewrite, text ="Change",bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
                    Ab2.place(x=140,y=100)
                    Ab4 = Button(root,command = Aend, text ="Exit",bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
                    Ab4.place(x=210,y=100)
                Ago3()
    else:
        ()
def launch():
    Ab5.destroy()
    Al1  = Label(root,text = "copywrite ATindustries",bg=colour,fg=colour2)
    Al1.place(x=160,y=50)
    root.update()
    time.sleep(1)
    Al1.configure(text="do not distribute")
    root.update()
    time.sleep(1)
    Al1.configure(text="ASCALON")
    root.update()
    time.sleep(2)
    Al1.place(x=160,y=1)
    root.update()
    Atb1.place(x=160,y=25)
    Al2.place(x=100,y=25)
    Al3.place(x=100,y=50)
    Atb2.place(x=160,y=50)
    Ab1.place(x=160,y=75)
Ab1= Button(root,text = "Go",command = Ago,bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
Al2 = Label(root,text="Username",bg=colour,fg=colour2)
Al3 = Label(root,text = "Password",bg=colour,fg=colour2)
Atb1 = Entry(root,bg=colour2,fg=colour)
Atb2 = Entry(root,bg=colour2,fg=colour)
Ab5 = Button(root,command = launch,text = "Launch",bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
Ab5.place(x=160,y=50)
root.mainloop()
