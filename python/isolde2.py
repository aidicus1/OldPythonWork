def encrypter(e):
    key1 = int(input(""))
    key3 = int(input(""))
    key4 = int(input(""))
    file = open(e+".txt","r")
    b =input("")
    file3 = open(b+".txt","w")
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
        print(splited)
        newlist = splited


        for y in range (len(splited)):
            print(y)
            if splited[y]!= "\n":
                file3.write (str(key4*((key3*splited[y])+key1)+key4)+",")
            else:
                ()
        file3.write("\n")




e = input("")
encrypter(e)