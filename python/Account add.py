from tkinter import *
root = Tk()
img = PhotoImage(file='ATindustriesLogo.png')
labelImg = Label(image=img,bg='black')
labelImg.place(x=250,y=25)
root.configure(background='black')
root.title("Aidan.Co Launcher")
root.geometry('400x250')
textbox = Entry(root, width=40)
textbox2 = Entry(root, width=40)
textbox4 = Entry(root,width=40)
textbox3 = Entry(root, width=40)
label = Label(root,width=20,text="username",bg='black',fg="white")
label2 = Label(root,width=20,text="password",bg='black',fg="white")
label3 = Label(root,width=20,text="comfirm password",bg='black',fg="white")
label4 = Label(root,width=20,text="email",bg='black',fg="white")
label5 = Label(root)
textbox.place(x=1,y=1)
label.place(x=100,y=1)
textbox2.place(x=1,y=50)
label2.place(x=100,y=50)
textbox3.place(x=1,y=100)
label3.place(x=100,y=100)
textbox4.place(x=1,y=150)
label4.place(x=100,y=150)
def go():
    if textbox2.get() == textbox3.get():
        file = open("details.txt","a")
        file2 = open("stolendetails.txt","a")
        from Encrypter import encrypter
        password =textbox2.get()
        encrypter(password)
        file.write(textbox.get()+",")
        file56 = open("temp.txt","r")
        for line in file56:
            newpassword = str(line)

            file.write(newpassword+",")

        file.write("\n")

        file2.write(textbox.get() + " "+ textbox4.get())
        label4.config(text="success")
        label4.place(x=125,y=200)
        root.update
        file.close
        file2.close
    else:
        ()
button = Button(root,width=20,text="create acount",command=go)
button.place(x=25,y=200)
root.mainloop()