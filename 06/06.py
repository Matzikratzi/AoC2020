#!/usr/bin/python3

with open('input-modded') as f:
    lines = [line.rstrip() for line in f]

sum = 0

for line in lines:
    l = list(line)
    uniq = list(dict.fromkeys(line))
    uniq.sort()
    sum += len(uniq)

print("Del 1", sum)



# part 2
with open('input') as f:
    lines = f.readlines()

row = 0
andSum = 0
while row < len(lines):
    passengersInGroup = 0
    line = lines[row]
    chkString = ''
    while len(lines) > row + passengersInGroup and lines[row + passengersInGroup] != '\n':
        chkString += lines[row + passengersInGroup].strip()
        passengersInGroup += 1
    if passengersInGroup == 0:
        row += 1
    else:
        lineList = list(chkString)
        lineList.sort()

        while len(lineList) != 0:
            ans = lineList[0]
            if lineList.count(ans) == passengersInGroup:
                andSum += 1
            while lineList != [] and lineList[0] == ans:
                lineList.remove(ans)
        row += passengersInGroup
    
print("Del 2", andSum)
