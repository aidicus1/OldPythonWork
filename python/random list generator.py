import random
file = open("numbers.txt","w")
y = random.randint(250000,300000)
for x in range (y):
    number = random.randint(1,(4*y))
    file.write(str(number)+",\n")

