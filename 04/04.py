#!/usr/bin/python3

import math

with open('input-fixed') as f:
    lines = [line.rstrip() for line in f]

i = 0
validPassports = 0
validNPC = 0

validFiels = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

while i < len(lines):
    local_validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl',
                         'pid', 'cid'] # make a local copy of expected fields
    line = lines[i]

    #now find check if enough fields are present
    list = line.split(' ')
    j = 0
    while j < len(list):
        pair = list[j].split(':')
        if pair[0] in local_validFields:
            local_validFields.remove(pair[0])
        j += 1
        
    if 0 == len(local_validFields):
        validPassports += 1
#        print(line)
    elif 1 == len(local_validFields) and local_validFields[0] == 'cid':
#        print(ĺine)
        validNPC += 1
    i +=1
print("answer:", validPassports+validNPC)
