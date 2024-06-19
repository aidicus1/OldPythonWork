file = open("test.txt","r")
filelist = []
dictionarylist = []
for line in file:
    data = line.split(" ")
    for x in range (len(data)):

        infile = 0
        y = 0
        for a in range (len(filelist)):
            listdata = filelist[a].split(",")

            if data[x] == listdata[0]:
                dictionarylist.append(int(listdata[1]))


                infile = 1

            else:
                y += 1
        if infile == 0:
            filelist.append(data[x]+","+str(y))
            dictionarylist.append(y)
        else:
            ()
file2  = open("filelist.txt","w")
for c in range (len(filelist)):
    file2.write(filelist[c]+" ")
file3 = open("dictionarylist.txt","w")
for b in range(len(dictionarylist)):
    file3.write(str(dictionarylist[b])+",")
file.close()
file2.close()
file3.close()