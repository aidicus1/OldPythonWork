def encrypter(incomplete):
    key1 = int(input(""))
    key3 = int(input(""))
    key4 = int(input(""))
    file3 = open(incomplete+".txt","r")
    for line2 in file3:



        splited= line2.split(",")

        print(splited)
        newlist = splited
        for y in range (len(splited)):
            print(y)
            if newlist[y] != "\n":
                newlist[y]= int((((int(splited[y])-key4)/key4)-key1)/key3)
                file = open("converter.txt","r")
                for line in file:
                    data = line.split(",")
                    if str(newlist[y]) == str(data[1]):
                        newlist[y] = data[0]
                    else:
                        ()
            else:
                ()

        file2 = open("decrypted.txt","w")
        for x in range (len(newlist)):
            file2.write(str(newlist[x]))
        file2.write(",\n")




E = input("")
encrypter(E)