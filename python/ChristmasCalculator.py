from tkinter import *
root = Tk()
def ChristmasCalcultor(willow):
    CClist =[]
    CCcost = 0
    print (CCcost)
    CCtb = Entry(willow)
    CCtb2 = Entry(willow)
    CCtb.pack()
    CCtb2.pack()
    def CCc1():
        CClist.append(CCtb.get())
        CCcost += int(CCtb2.get())

    CCb= Button(willow,text = "add to list",command=CCc1).pack()
    def CCc2():
        print(CClist)
        print(CCcost)
    CCb2=Button(willow,text = "total",command = CCc2).pack()
ChristmasCalcultor(root)
root.mainloop()
