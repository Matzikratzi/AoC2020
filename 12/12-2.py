#!/usr/bin/python3


def Movement(pos, direction, instruction):
    action = instruction[0]
    value  = int(instruction[1:])
    newPos = pos.copy()
    newDirection = direction.copy()
    print(instruction)
    print(action)
    print(value)
    print(position)
    print(direction)
          
    if action == 'N':
        newDirection[1] += value
    elif action == 'S':
        newDirection[1] -= value
    elif action == 'E':
        newDirection[0] += value
    elif action == 'W':
        newDirection[0] -= value
    elif action == 'F':
        newPos[0] += value*direction[0]
        newPos[1] += value*direction[1]
    else:                       # Change of direction
        rots = value / 90
        r = 0
        tmpDir = newDirection.copy()
        if action == 'R':
            while r < rots: 
                # clockwise change
                tmpDir[0] = newDirection[1]
                tmpDir[1] = -newDirection[0]
                newDirection[0] = tmpDir[0]
                newDirection[1] = tmpDir[1]
                r += 1
        else:
            while r < rots: 
                # clockwise change
                tmpDir[0] = -newDirection[1]
                tmpDir[1] = newDirection[0]
                newDirection[0] = tmpDir[0]
                newDirection[1] = tmpDir[1]
                r += 1
    return newPos, newDirection

with open('input') as f:
#with open('input-small') as f:
    data = [line.rstrip() for line in f]

direction = [10, 1] # E=[1,0], N=[0,1] ..
position = [0,0]


for row in data:
    # print(position)
    # print(direction)
    # print(row)
    position, direction = Movement(position, direction, row)

print('Position:', position)
print('Manhattan distance:', abs(position[0])+abs(position[1]))

        
