from tkinter import *
root = Tk()
def grail(root):
    def guinevere():
        Groot = Tk()
        Gtb4 = Entry(Groot)
        Gtb5 = Entry(Groot)
        Gtb4.pack()
        Gtb5.pack()
        def guineverego():
            file5=open("details.txt","r")
            import os
            username = Gtb4.get()
            password = Gtb5.get()
            from Encrypter import encrypter
            encrypter(password)
            file56 = open("temp.txt","r")
            for line in file56:
                newpassword = line
            for line in file5:
                data = line.split(",")
                if username == data[0] and newpassword == data[1]:
                    splited = ','.join(password)
                    splited= splited.split(",")
                    file = open("converter.txt","r")
                    for line in file:
                        data=line.split(",")
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
                    e = Gtb1.get()
                    file = open(e+".txt","r")
                    file3 = open("encrypted.txt","w")
                    for line in file:
                        splited = ','.join(line)
                        splited= splited.split(",")
                        file2 = open("converter.txt","r")
                        for line in file2:
                            data=line.split(",")
                            for x in range(len(splited)):
                                if splited[x] == data[0]:
                                    splited[x] = int(data[1])
                                else:
                                    ()
                        file2.close()
                        newlist = splited
                        for y in range (len(splited)):
                            if splited[y]!= "\n":
                                write =(str(key4*((key3*splited[y])+key1)+key4)+",")
                                file3.write (write)
                            else:
                                ()
                        file3.write("\n")
                    file.close()
                    file3.close()
                    os.remove(e+".txt")
                    os.rename("encrypted.txt",e+".txt")
            Groot.destroy()
        Gb3 = Button(Groot, text="ok", command = guineverego)
        Gb3.pack()
    def lancelot():
        Lroot = Tk()
        Gtb2 = Entry(Lroot)
        Gtb3 = Entry(Lroot)
        Gtb2.pack()
        Gtb3.pack()
        def lancelotgo():
            file5=open("details.txt","r")
            import os
            username = Gtb2.get()
            password = Gtb3.get()
            if username == " ":
                ()
            else:
                from Encrypter import encrypter
                encrypter(password)
                file56 = open("temp.txt","r")
                for line in file56:
                    newpassword = line
                for line in file5:
                    data = line.split(",")
                    if username == data[0] and newpassword == data[1]:
                        splited = ','.join(password)
                        splited= splited.split(",")
                        file = open("converter.txt","r")
                        for line in file:
                            data=line.split(",")
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
                        e = Gtb1.get()
                        file = open(e+".txt","r")
                        file2 = open("decrypted.txt","w")
                        file2.close()
                        for line in file:
                            splited= line.split(",")
                            newlist = splited
                            for y in range (len(splited)):
                                if newlist[y] != "\n":
                                    newlist[y]= int((((int(splited[y])-key4)/key4)-key1)/key3)
                                    file4 = open("converter.txt","r")
                                    for line2 in file4:
                                        data = line2.split(",")
                                        if str(newlist[y]) == str(data[1]):
                                            newlist[y] = data[0]
                                        else:
                                            ()
                                else:
                                    ()
                            file2 = open("decrypted.txt","a")
                            for x in range (len(newlist)):
                                file2.write(str(newlist[x]))
                        file.close()
                        file2.close()
                        os.remove(e+".txt")
                        os.rename("decrypted.txt",e+".txt")
                Lroot.destroy()
        Gb1 = Button(Lroot, text="ok", command = lancelotgo)
        Gb1.pack()
    Gtb1 = Entry(root)
    Gtb1.pack()
    Gb2 = Button(root, text = "decrypt", command = lancelot)
    Gb2.pack()
    Gb4 = Button(root, text = "encrypt", command  = guinevere)
    Gb4.pack()
grail(root)
root.mainloop()




