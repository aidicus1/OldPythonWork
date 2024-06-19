from tkinter import *
import random
import time
root=Tk()

def begin(root):


    file = open("result.txt","w")
    file.close
    file=open("numoftries.txt","w")
    file.close
    colour=("blue")
    colour2=("grey")
    listnum = ("0")
    img = PhotoImage(file='ATindustriesLogo.png')
    labelImg = Label(image=img,bg=colour)
    labelImg.place(x=370)
    root.configure(background=colour)
    root.title("Aidan.Co Launcher")
    root.geometry('445x130')
    Llabel = Label(root,text="setup ready",bg=colour,fg=colour2)
    Llabel.place(x=1,y=50)
    def launching():
        Lbutton.destroy()
        Llabel.configure(text="beggining setup")
        root.update()
        time.sleep(2)
        Llabel.configure(text="protected by P.E.S.T")
        root.update()
        time.sleep(2)
        Llabel.configure(text="Made by AidanCo")
        root.update()
        time.sleep(2)
        Llabel.configure(text="a subsidary of ATindustries")
        root.update()
        time.sleep(2)
        Llabel.configure(text="all rights reserved")
        root.update()
        time.sleep(2)
        Llabel.configure(text="setup complete")
        root.update()
        time.sleep(2)
        Llabel.configure(text="firering photon cannons")
        time.sleep(2)
        root.update()
        Llabel.configure(text="Launching")
        time.sleep(2)
        root.update()
        Llabel.destroy()
        textbox3.place(x=100,y=50)
        textbox4.place(x=100, y=1)
        label6.place(x=1, y=1)
        label5.place(x=1,y=50)
        button8.place(x=210,y=75)
        button7.place(x=130,y=75)

    Lbutton = Button(root, text="Launch",width=10, height=1,command=launching,bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)
    Lbutton.place(x=100,y=50)

    label6 = Label(root,text="enter username",bg=colour,fg=colour2)

    textbox4 = Entry(root ,width=44,bg=colour2,fg=colour)

    label5 = Label(root,text="enter password",bg=colour,fg=colour2)

    textbox3 = Entry(root, width=44,bg=colour2,fg=colour)

    def logon():
        if textbox4.get() == "" or textbox3.get() == "":
            ()
        else:
            file2=open("details.txt","r")
            for line in file2:
                time.sleep(1)
                data = line.split(",")
                from Encrypter import encrypter
                password =textbox3.get()
                encrypter(password)
                file56 = open("temp.txt","r")
                for line in file56:
                    newpassword = line



                if data[0] == textbox4.get() and data[1] == newpassword:
                    def destroyer():
                        button4.destroy()
                        button9.destroy()
                        button10.destroy()
                        button11.destroy()
                        button12.destroy()
                        button13.destroy()
                        button14.destroy()


                    textbox3.destroy()
                    textbox4.destroy()
                    button7.destroy()
                    button8.destroy()
                    labelImg.destroy()
                    label5.destroy()
                    label6.destroy()
                    root.configure(background=colour2)
                    file2.close
                    root.title("THE USEFUL CODE")
                    root.geometry('1000x150')
                    def start():
                        destroyer()

                        from replacementnamegenerator import randomname
                        randomname(root)
                    def startbreaker():
                        destroyer()

                        from Breacker import breaker
                        breaker(root)
                    def startchristmas():
                        destroyer()
                        from ChristmasCardWriter import ChristmasCardWriter
                        ChristmasCardWriter(root)
                    def startbubble():
                        destroyer()
                        from bubblefilesort import bubblefilesort
                        bubblefilesort(root)
                    def startinsertion():
                        destroyer()
                        from inserttionfilesort import insertionfilesort
                        insertionfilesort(root)
                    def startlinear():
                        destroyer()
                        from Linearsearch import Linearsearch
                        Linearsearch(root)
                    def startmean():
                        destroyer()
                        from mean import mean
                        mean(root)
                    button4 = Button(root, text="Random name generator", width=20, height=2,command=start,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button4.place(x=50)
                    button9 = Button(root, text="Breaker", width=20, height=2,command=startbreaker,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button9.place(x=300)
                    button10 = Button(root, text="Christmas", width=20, height=2,command=startchristmas,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button10.place(x=550)
                    button11=  Button(root, text="bubble", width=20, height=2,command=startbubble,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button11.place(y =50 ,x =50)
                    button12 = Button(root, text="insertion", width=20, height=2,command=startinsertion,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button12.place(y=50,x=300)
                    button13 = Button(root, text="lineat", width=20, height=2,command=startlinear,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button13.place(y=50,x=550)
                    button14 = Button(root, text="mean", width=20, height=2,command=startmean,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
                    button14.place(y = 100,x=50)





                    root.update

                else:
                    ()
    button7 = Button(root, text="Login",width=10, height=1,command=logon,bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)

    def end2():
        root.destroy()
    button8= Button(root, text="EXIT",width =10,height=1,command=end2,bg=colour2,activebackground=colour,fg=colour,activeforeground=colour)

    root.mainloop()
begin(root)
