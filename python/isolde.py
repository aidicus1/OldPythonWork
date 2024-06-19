def encrypter(incomplete):
    key1 = int(input(""))
    key3 = int(input(""))
    key4 = int(input(""))


    splited = ','.join(incomplete)
    splited= splited.split(",")
    file = open("converter.txt","r")
    for line in file:
        data=line.split(",")
        for x in range(len(splited)):
            if splited[x] == data[0]:
                splited[x] = int(data[1])
            else:
                ()
    file.close()
    print(splited)


    encrypt = key1
    print(encrypt)
    newerlist = []
    for y in range (len(splited)):
        count = 0
        top = 0
        encrypt = encrypt + splited[y]
        print(encrypt)
        for a in range (encrypt):

            if count < 90 and top == 0:
                count += 1
            elif count == 0:
                count +=1
                top = 0
            elif count >= 90:
                count -= 1
                top = 1

            elif top == 1 and count > 0:
                count -=1


            else:
                ()
        newerlist.append(count)
    encrypt = encrypt * key3
    print(encrypt)
    newlist = []
    print(newerlist)
    for p in range (len(splited)):
        count = 0
        top = 0
        print(newerlist)
        encrypt = encrypt + newerlist[p]
        print(encrypt)
        encrypt = encrypt * key4
        print(encrypt)
        for a in range (encrypt):

            if count < 90 and top == 0:
                count += 1
            elif count == 0:
                count +=1
                top = 0
            elif count >= 90:
                count -= 1
                top = 1

            elif top == 1 and count > 0:
                count -=1


            else:
                ()

        newlist.append(count)
    print(newlist)

    finallist = newlist
    for c in range (len(newlist)):
        file = open("converter.txt","r")

        for line in file:

            data = line.split(",")

            if finallist[c] == int(data[1]):


                finallist[c] = data[0]

            else:
                ()
        file.close()
    file = open("temp.txt","w")
    file.write(str(top)+","+str(encrypt)+",")
    for x in range (len(finallist)):
        file.write(finallist[x])
    file.close
E = input("")
encrypter(E)