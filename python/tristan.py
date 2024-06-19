def decrypter(incomplete):
    key1 = int(input(""))

    key3 = int(input(""))
    key4 = int(input(""))


    spliting=incomplete.split(",")
    splited = ','.join(spliting[2])
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
    print(len(splited))
    print(splited)
    encrypt =int(int(spliting[1]))

    newerlist = []

    for y in range (len(splited)):
        count = 0
        top = 1




        print(encrypt)

        encrypt = int(encrypt / key4)
        encrypt = encrypt - splited[len(splited)-y-1]
        print(splited[len(splited)-y-1])
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
        print(count)
        newerlist.append(count)




    print(newerlist)
    encrypt = int(encrypt / key3)

    newlist = []
    for p in range (1,len(splited)):
        count = 0
        top = 0

        encrypt = encrypt - newerlist[len(splited)-p-1]


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
    file = open("temp2.txt","w")
    for x in range (len(finallist)):
        file.write(str(finallist[x]))
    file.close
E = input("")
decrypter(E)