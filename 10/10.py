#!/usr/bin/python3

with open('input') as f:
#with open('small-input') as f:
    data = [int(line.rstrip()) for line in f]
data.sort()
data.append(data[-1] + 3)

diffBins = [0, 0, 0, 0, 0, 0]
diffData = []
numDiff1 = 0
numDiff3 = 0
i = 0
prev = 0
lastDiff = 0
sameDiff = 0
while i < len(data):
    current = data[i]
    diff = current - prev
    if diff == lastDiff:
        sameDiff += 1
    else:
        if lastDiff == 1:
            diffBins[sameDiff] += 1
        lastDiff = diff
        sameDiff = 1
    diffData.append(diff)
    if diff == 1:
        numDiff1 += 1
    elif diff == 3:
        numDiff3 += 1
    else:
        print(diff)
    i += 1
    prev = current

print('First Answer:',numDiff3 * numDiff1)
# This is calculated by hand 
pathsInGroup = [0, 1, 2, 4, 7]

numOfValidPaths = 1
i = 0
while i < len(pathsInGroup):
    numOfValidPaths *= pathsInGroup[i]**diffBins[i]
    i += 1
    
print('Second Answer:', numOfValidPaths)
