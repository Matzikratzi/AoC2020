#!/usr/bin/python3

import math

with open('input') as f:
    lines = [line.rstrip() for line in f]


i = 0

while i < len(lines):
    num1 = int(lines[i])
    j = i + 1
    while j < len(lines):
        num2 = int(lines[j])
        if num1 + num2 == 2020:
            print(num1, num2, num1*num2)
        j += 1
    i += 1

i = 0

while i < len(lines):
    num1 = int(lines[i])
    j = i + 1
    while j < len(lines):
        num2 = int(lines[j])
        k = j + 1
        while k < len(lines):
            num3 = int(lines[k])
            if num1 + num2 + num3 == 2020:
                print(num1, num2, num3, num1*num2*num3)
            k +=1
        j += 1
    i += 1
