file = open("converter.txt","r")
file2=open("converter2.txt","w")
for line in file:
    line2 = "¬".join(line)
    line2 = line2.split("¬")
    for x in range (len(line2)):
        if line2[x] == ",":
            file2.write("¬")
        else:
            file2.write(line2[x])
file2.close()