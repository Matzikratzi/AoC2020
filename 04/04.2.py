#!/usr/bin/python3

import math

import re
def countnonoverlappingrematches(pattern, thestring):
  return re.subn(pattern, '', thestring)[1]

def checker(pair):
    valid = False
    validEyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    key = pair[0]
    if key == 'byr':
        year = pair[1]
        if year.isnumeric():
            numYear = int(year)
            if numYear > 1919 and numYear < 2003:
                valid = True
    elif key == 'iyr':
        year = pair[1]
        if year.isnumeric():
            numYear = int(year)
            if numYear > 2009 and numYear < 2021:
                valid = True
    elif key == 'eyr':
        year = pair[1]
        if year.isnumeric():
            numYear = int(year)
            if numYear > 2012 and numYear < 2031:
                valid = True
    elif key == 'hgt':
        hgt = pair[1]
        if len(hgt) == 5 and hgt[:3].isnumeric() and hgt[3:] == 'cm':
            l = int(hgt[:3])
            if l > 149 and l < 194:
                valid = True
        if len(hgt) == 4 and hgt[:2].isnumeric() and hgt[2:] == 'in':
            l = int(hgt[:2])
            if l > 58 and l < 77:
                valid = True
    elif key == 'hcl':
        clr = pair[1]
        if clr[0] == '#' and len(clr) == 7:
            hnum = clr[1:]
            occ = countnonoverlappingrematches('[0-9a-f]', hnum)
            if occ == 6:
                valid = True
    elif key == 'ecl':
        clr = pair[1]
        if len(clr) == 3 and clr in validEyeColours:
            valid = True
    elif key == 'pid':
        num = pair[1]
        if num.isnumeric() and len(num) == 9:
            valid = True
    elif key == 'cid':
        valid = True
    else:
        valid = True
        
    return valid

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
            if checker(pair) == True:
                local_validFields.remove(pair[0])
            else:
                print(line)
                break
        j += 1
        
    if 0 == len(local_validFields):
        validPassports += 1
#        print(line)
    elif 1 == len(local_validFields) and local_validFields[0] == 'cid':
#        print(ĺine)
        validNPC += 1
    i +=1
print("answer:", validPassports+validNPC)
