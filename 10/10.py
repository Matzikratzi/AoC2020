#!/usr/bin/python3

with open('input-sorted') as f:
#with open('small-input') as f:
    data = [line.rstrip() for line in f]

numDiff1 = 1
numDiff3 = 1
i = 1
while i < len(data):
    diff = int(data[i]) - int(data[i-1])
    if diff == 1:
        numDiff1 += 1
    elif diff == 3:
        numDiff3 += 1
    else:
        print(diff)
    i += 1
print(numDiff1)
print(numDiff3)
print('First Answer:',numDiff3 * numDiff1)

##################################################
# Second solution

with open('input-sorted') as f:
#with open('small-input') as f:
    data = [line.rstrip() for line in f]

