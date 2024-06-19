item = input("input")
from Encrypter import encrypter
encrypter(item)

file = open("temp.txt","r")
for line in file:
    print(line)

