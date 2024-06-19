def encrypter(incomplete):
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
    encrypt = 2
    newerlist = []
    for y in range (len(splited)):
        count = 0
        top = 0
        encrypt = encrypt + splited[y]
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
    encrypt = encrypt * newerlist[len(newerlist)-1]
    newlist = []
    for p in range (len(splited)):
        count = 0
        top = 0
        encrypt = encrypt + newerlist[p]
        encrypt = encrypt * 2
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
    file = open("temp.txt","w")
    for x in range (len(finallist)):
        file.write(finallist[x])
    file.close
