def percival(filename):
    filelist = []
    dictionarylist = []
    y = 0
    Pflie=open(filename+".txt","r")
    for line in Pflie:
        data =line.split(",")
        for x in range (len(data)):
            y+=1
            if data[x] != "\n":
                infile = 0
                for a in range (len(filelist)):
                    listdata = filelist[a].split(",")
                    if data[x] == listdata[0]:
                        dictionarylist.append(int(listdata[1]))
                        infile = 1
                    else:
                        ()
                if infile == 0:
                    filelist.append(data[x]+","+str(y))
                    dictionarylist.append(y)
                else:
                    ()
            elif data[x] == "\n":

                dictionarylist.append(y)
                filelist.append("/n,"+str(y))
            else:
                ()
    Pfile2  = open(filename+"list.txt","w")
    for c in range (len(filelist)):
        Pfile2.write(filelist[c]+" ")
    Pfile3 = open(filename+"dictionary.txt","w")
    for b in range(len(dictionarylist)):
        Pfile3.write(str(dictionarylist[b])+",")
    Pflie.close()
    Pfile2.close()
    Pfile3.close()