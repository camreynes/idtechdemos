import random

numList = [55,57,62,2]

numList.append(90) #append adds to end of list
numList.insert(0,80) #inserts at start


print("full list: " + str(numList)) #print the full list
print("second position of list: " + str(numList[1]))
                    #print the second position, computers
                    #start counting at 0
lenList = len(numList) #length of list
print("length of list: " + str(lenList))

randList = []
for i in range(0,19):
    randList.append(random.randint(0,100))

print(randList)