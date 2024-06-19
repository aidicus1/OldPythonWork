import os
def gawayne(filename):
    Gfile= open(filename+"list.txt","r")
    Gfile2 = open(filename+"dictionary.txt","r")
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
    Gfile3 = open(filename+".txt","w")
    for x in range(len(Glist3)):
        Gfile3.write(Glist3[x]+",")
    Gfile.close()
    Gfile2.close()
    Gfile3.close()
    os.remove(filename+"list.txt")
    os.remove(filename+"dictionary.txt")
