from datetime import datetime
start = datetime.now()
def unbreaker():
    encrypt = 2
    newerlist = []
    for y in range (len(splited)):
        count = 0
        top = 0
        encrypt = encrypt + splited[y]
        emcrypt= encrypt  * 2
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
    if newerlist == spliting:
        correctlist = splited
    else:
        ()
import random
crack = input("enter")
spliting = ','.join(crack)
splited= spliting.split(",")
for a in range (91):
    splited[0] = random.randint(0,91)
    if len(splited) > 1:
        for b in range (91):
            splited[1] = random.randint(0,91)
            if len(splited) > 2:
                for c in range (91):
                    splited[2] = random.randint(0,91)
                    if len(splited) > 3:
                        for d in range (91):
                            splited[3] = random.randint(0,91)
                            if len(splited) > 4:
                                for e in range (91):
                                    splited[4] = random.randint(0,91)
                                    if len(splited) > 5:
                                        for f in range (91):
                                            splited[5] = random.randint(0,91)
                                            if len(splited) > 6:
                                                for g in range (91):
                                                    splited[6] = random.randint(0,91)
                                                    if len(splited) > 7:
                                                        for h in range (91):
                                                            splited[7] = random.randint(0,91)
                                                            if len(splited) > 8:
                                                                for i in range (91):
                                                                    splited[8] = random.randint(0,91)
                                                                    if len(splited) > 9:
                                                                        for j in range (91):
                                                                            splited[9] = random.randint(0,91)
                                                                            if len(splited) > 10:
                                                                                for k in range (91):
                                                                                    splited[10] = random.randint(0,91)
                                                                                    if len(splited) > 11:
                                                                                        for l in range (91):
                                                                                            splited[11] = random.randint(0,91)
                                                                                            if len(splited) > 12:
                                                                                                for m in range (91):
                                                                                                    splited[12] = random.randint(0,91)
                                                                                                    if len(splited) > 13:
                                                                                                        for o in range (91):
                                                                                                            splited[13] = random.randint(0,91)
                                                                                                            if len(splited) > 14:
                                                                                                                for p in range (91):
                                                                                                                    splited[14] = random.randint(0,91)
                                                                                                                    if len(splited) > 15:
                                                                                                                        for q in range (91):
                                                                                                                            splited[15] = random.randint(0,91)
                                                                                                                            if len(splited) > 16:
                                                                                                                                for r in range (91):
                                                                                                                                    splited[16] = random.randint(0,91)
                                                                                                                            else:
                                                                                                                                unbreaker()
                                                                                                                        else:
                                                                                                                            unbreaker()
                                                                                                                    else:
                                                                                                                        unbreaker()
                                                                                                                else:
                                                                                                                    unbreaker()
                                                                                                            else:
                                                                                                                unbreaker()
                                                                                                        else:
                                                                                                            unbreaker()
                                                                                                    else:
                                                                                                        unbreaker()
                                                                                                else:
                                                                                                    unbreaker()
                                                                                            else:
                                                                                                unbreaker()
                                                                                        else:
                                                                                            unbreaker()
                                                                                    else:
                                                                                        unbreaker()
                                                                                else:
                                                                                    unbreaker()
                                                                            else:
                                                                                unbreaker()
                                                                        else:
                                                                            unbreaker()
                                                                    else:
                                                                        unbreaker()
                                                                else:
                                                                    unbreaker()
                                                            else:
                                                                unbreaker()
                                                        else:
                                                            unbreaker()
                                                    else:
                                                        unbreaker()
                                                else:
                                                    unbreaker()
                                            else:
                                                unbreaker()
                                        else:
                                            unbreaker()
                                    else:
                                        unbreaker()
                                else:
                                    unbreaker()
                            else:
                                unbreaker()
                        else:
                            unbreaker()
                    else:
                        unbreaker()
                else:
                    unbreaker()
            else:
                unbreaker()
        else:
            unbreaker()
    else:
        unbreaker()
print (correctlist)
end = datetime.now()

print(f"Time taken in (hh:mm:ss.ms) is {end - start}")



