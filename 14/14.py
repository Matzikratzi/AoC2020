#!/usr/bin/python3
import math

# 36 bit values

memory = [0] * 100000
mask   = ''


with open('input') as f:
#with open('input-small') as f:
    program = [line.rstrip() for line in f]

def ApplyMaskToValue(val, m):
    bval = bin(val)
    lbval = list(bval[2:])
#    value = ['0b'] + ['0'] * (36 - len(lbval))
    vList = ['0'] * (36 - len(lbval)) + lbval

    mList = list(m)
    i =  0
    while i < len(mList):
        mBit = mList[i]
        if mBit != 'X':
            vList[i] = mBit
        i += 1
    sVal = "".join(vList)
    return int(sVal, 2)
    
def Parser():
    global mask
    for instruction in program:
        if 'mask' in instruction:
            mask = instruction[7:]
        else:
            # memory set command
            i = 5
            while i < 10:
                if instruction[i] == ']':
                    address = int(instruction[4:i])
                    value = int(instruction[i+4:])
                    break
                i += 1
            val = ApplyMaskToValue(value, mask)
            memory[address] = val


Parser()

summa = 0
for v in memory:
    summa += v
print(summa)
