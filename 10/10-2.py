#!/usr/bin/python3

numOfPoss = 0

def nextChecker(adaptorList, adaptorInd, maxInd, prevJolt, soFarList):
    ind = 0
    while ind < 3 and ind + adaptorInd < maxInd:
        nextInd = ind + adaptorInd
        nextJolt = int(adaptorList[nextInd])
        if nextJolt - prevJolt <= 3:
            soFarList.append(nextJolt)
            nextChecker(adaptorList, nextInd+1, maxInd, nextJolt, soFarList)
        ind += 1
    if ind + adaptorInd == maxInd-1:
        numOfPoss += 1

with open('input-small') as f:
#with open('small-input') as f:
    data = [line.rstrip() for line in f]

nextChecker(data, 0, len(data), 0, [])
print(numOfPoss)
