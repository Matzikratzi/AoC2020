#!/usr/bin/python3

import math

with open('input') as f:
    lines = [line.rstrip() for line in f]

i = 0
pos = 0
trees = 0
while i < len(lines):
    line = lines[i]
    
    if line[pos%len(line)] == "#":
            trees += 1
    i += 1
    pos += 3


print("First solution", trees)
####################


    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.


downs = [1, 1, 1, 1, 2]
rigths = [1, 3, 5, 7, 1]

product = 1
run = 0

while run < 5:
    i = 0
    trees = 0
    pos = 0
    down = downs[run]
    rigth = rigths[run]

    while i < len(lines):
        line = lines[i]
    
        if line[pos%len(line)] == "#":
            trees += 1
        i += down
        pos += rigth
    run += 1
    
    product *= trees

print("Second solution", product)
####################
