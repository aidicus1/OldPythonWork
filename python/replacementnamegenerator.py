from tkinter import *
import random
def randomname(mumba):
    colour = ("blue")
    colour2= ("grey")
    mumba.geometry("200x200")
    List=["end"]
    Label3 = Label(mumba,text=("Y12"),bg=colour,fg=colour2).place(x=15,y=5)
    Label4 = Label(mumba,text=("Y13"),bg=colour,fg=colour2).place(x=105,y=5)
    def go():
        go2=0
        while go2 == 0:
            file = open("year12.txt","r")
            x = 0
            for line in file:
                x += 1
            y= 0
            x=random.randint(0,x)
            file = open("year12.txt","r")
            for line in file:
                y += 1
                if y == x and line in List:
                    ()
                elif y==x:
                    Label1.configure(text=line)
                    mumba.update()
                    go2 += 1
                    List.append(line)
                else:
                    ()
    Button1 = Button(mumba,text= "select name", command = go,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
    Button1.place(x=10,y=35)
    Label1= Label(mumba,text="The name is",bg=colour2,fg=colour)
    Label1.place(x=10,y=65)
    List2=["end"]
    def go1():
        go3=0
        while go3 == 0:
            file = open("year13.txt","r")
            x = 0
            for line in file:
                x += 1
            y= 0
            x=random.randint(0,x)
            file = open("year13.txt","r")
            for line in file:
                y += 1
                if y == x and line in List2:
                    ()
                elif y==x:
                    Label2.configure(text=line)
                    mumba.update()
                    go3 += 1
                    List2.append(line)
                else:
                    ()
    def RNGend():
        mumba.destroy()
    Button2 = Button(mumba,text= "select name", command = go1,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
    Button2.place(x=100,y=35)
    RNGbutton3 = Button(mumba,text="exit",command = RNGend,bg=colour,activebackground=colour2,fg=colour2,activeforeground=colour2)
    RNGbutton3.place(x=50,y=80)
    Label2= Label(mumba,text="The name is",bg=colour2,fg=colour)
    Label2.place(x=100,y=65)
    mumba.update



