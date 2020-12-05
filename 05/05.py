#!/usr/bin/python3

with open('input') as f:
    lines = [line.rstrip() for line in f]

binlines = []
    
for line in lines:
    binline = line.replace('F', '0')
    binline = binline.replace('B', '1')
    binline = binline.replace('L', '0')
    binline = binline.replace('R', '1')
    binlines.append(binline)


binlines.sort()

print(int(binlines[-1], 2))

checkID = int(binlines[0], 2) - 1

for sortedline in binlines:
    ID = int(sortedline, 2)
    if ID != checkID + 1:
        print(int(ID) - 1)
    checkID = ID
