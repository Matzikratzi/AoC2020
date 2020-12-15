#!/usr/bin/python3
import math

# 36 bit values

# sequence     = [-471147114711, 0, 3, 6]

# numInSeq     = 4                    # Present indNumber (index + 1) to be considered
# saidLast = 6

sequence     = [-471147114711, 14,8,16,0,1,17]
numInSeq = 7
saidLast = 17


#saidRecently = [-1] * 2021          # indNumber when number was last said
saidRecently = [-1] * 30000009          # indNumber when number was last said


def Initiate():
    i = 1
    while i < len(sequence)-1:
        saidRecently[sequence[i]] = i
        i += 1

def NextNumber(presentIndNum):
    global saidLast
    #print('saidLast',saidLast)
    lastTime = saidRecently[saidLast]
    saidRecently[saidLast] = presentIndNum - 1
#    print('lasttime',lastTime)
    if lastTime ==  -1:
        newNum = 0
    else:
        newNum = presentIndNum - lastTime - 1
#    print('newnum',newNum)
    saidLast = newNum
    return newNum

Initiate()

while numInSeq < 30000009:
    number = NextNumber(numInSeq)
    if numInSeq > 29999999:
        print(numInSeq, number)
    numInSeq += 1

