import random
import time
#when we want to use a random number, we first need to import
#the random package at the start of the program

i = 0

while True:
    num = random.randint(0,1) #this is how we make a random number
    print(num, end = " ") #we can specify end so it doesnt make a new line
    time.sleep(0.005) #delay between each number
    i += 1
    if i == 100:
        print()
        i = 0
