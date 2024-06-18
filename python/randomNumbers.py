import random
import time
#when we want to use a random number, we first need to import
#the random package at the start of the program

i = 0

while True:
    num = random.randint(0,999) #this is how we make a random number
    print(num, end = " ")
    time.sleep(0.01)
    i += 1
    if i == 50:
        print()
        i = 0
