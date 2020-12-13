#!/usr/bin/python3
import math

def findIndexOfBiggest(ID):
    biggest = 0
    indexOfBiggest = 0
    i = 0
    while i < len(ID):
        val = ID[i]
        if val > biggest:
            biggest = val
            indexOfBiggest = i
        i += 1
    return indexOfBiggest

with open('input') as f:
#with open('input-small') as f:
    data = [line.rstrip() for line in f]

earliest = int(data[0])
#data[1] = '1789,37,47,1889'

IDs = data[1].split(',')



compID  = []
compInd = []

i = 0
while i < len(IDs):
    ID = IDs[i]
    if ID != 'x':
#        print(i, ID)
        compID.append(int(ID))
        compInd.append(i)
    i += 1

sortedIndices = sorted(range(len(compID)), key=lambda k: compID[k], reverse=True)

print('compID:\t\t', compID)
print('compInd:\t', compInd)

print(sortedIndices)


#[listofLines[i] for i in sortedIndex]
idList = [compID[i] for i in sortedIndices]
indList = [compInd[i] for i in sortedIndices]

print(idList)
print(indList)

startN = 0
n = startN
while True:
    t = n * idList[0] - indList[0]
    if (    (t + indList[1]) % idList[1] == 0
        and (t + indList[2]) % idList[2] == 0
        and (t + indList[3]) % idList[3] == 0
        and (t + indList[4]) % idList[4] == 0
    ):
        print('tested time', t, n)
        if ((t + indList[5]) % idList[5] == 0
            and (t + indList[6]) % idList[6] == 0
            and (t + indList[7]) % idList[7] == 0
            and (t + indList[8]) % idList[8] == 0
            ):

            print('solution:',t)
            break
    n += 1
