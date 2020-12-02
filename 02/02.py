#!/usr/bin/python3

import math

with open('input') as f:
    lines = [line.rstrip() for line in f]

numOfPasswdOk = 0
i = 0

while i < len(lines):
    line = lines[i]
    list = line.split(': ')

    password = list[1]
    rule = list[0]

    ruleList = rule.split(' ')
    occurences = ruleList[0]
    character  = ruleList[1]

    lowOcc = int(occurences.split('-')[0])
    highOcc = int(occurences.split('-')[1])

    occInPw = password.count(character)

    if lowOcc <= occInPw and highOcc >= occInPw:
        numOfPasswdOk += 1

    i += 1

print("First solution", numOfPasswdOk)
####################

numOfPasswdOk = 0
i = 0

while i < len(lines):
    line = lines[i]
    list = line.split(': ')

    password = list[1]
    rule = list[0]

    ruleList   = rule.split(' ')
    positions  = ruleList[0]
    character  = ruleList[1]

    lowPos = int(positions.split('-')[0]) - 1
    highPos = int(positions.split('-')[1]) - 1

    if bool(character == password[lowPos]) != bool(character == password[highPos]):
        numOfPasswdOk += 1

    i += 1

print("Second solution", numOfPasswdOk)
