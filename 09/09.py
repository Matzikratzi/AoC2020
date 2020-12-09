#!/usr/bin/python3

checkList = []

with open('input') as f:
#with open('small-input') as f:
    data = [line.rstrip() for line in f]

def checker(ind):
    dataToBeCtrl = data[ind]
    firstTermInd = ind - preambLen
    while firstTermInd < ind:
        firstTerm = data[firstTermInd]
        secondTermInd = firstTermInd + 1
        while secondTermInd < ind:
            secondTerm = data[secondTermInd]
            if int(dataToBeCtrl) ==  int(firstTerm) + int(secondTerm):
                return True, firstTermInd, secondTermInd
            secondTermInd += 1
        firstTermInd += 1
    return False, -1, -1

def continFinder(acc):
    ind = 0
    while ind < len(data):
        localAcc = 0
        secondInd = ind
        while secondInd < len(data) and localAcc < acc:
            localAcc += int(data[secondInd])
            secondInd += 1
        if localAcc == acc:
            return True, ind, secondInd - 1
        ind += 1
    return False, -1, -1
    
preambLen = 25
ind = preambLen

while ind < len(data):
    ok, firstTermInd, secondTermInd = checker(ind)
    if ok == False:
        break
    ind += 1
print("First answer", data[ind])

invalidNumber = int(data[ind])

result, firstInd, lastInd = continFinder(invalidNumber)

continousList = []
i = 0
while firstInd + i <= lastInd:
    continousList.append(int(data[firstInd + i]))
    i += 1

continousList.sort()
print('Second answer', continousList[0]+continousList[-1])
