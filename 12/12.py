#!/usr/bin/python3

def Movement(pos, direction, instruction):
    action = instruction[0]
    value  = int(instruction[1:])
    newPos = pos.copy()
    newDirection = direction
    if action == 'N':
        newPos[1] += value
    elif action == 'S':
        newPos[1] -= value
    elif action == 'E':
        newPos[0] += value
    elif action == 'W':
        newPos[0] -= value
    elif action == 'F':
        if direction == 90:     # N
            newPos[1] += value
        elif direction == 270:  # S
            newPos[1] -= value
        elif direction == 0:      # E
            newPos[0] += value
        else: # W
            newPos[0] -= value
    else:                       # Change of direction
        if action == 'R':
            # clockwise change
            newDirection -= value
            newDirection += 360
            newDirection %= 360
        else:
            # anti clockwise
            newDirection += value
            newDirection %= 360
    return newPos, newDirection

with open('input') as f:
#with open('input-small') as f:
    data = [line.rstrip() for line in f]

direction = 0 # E=0, N=90, W=180, S=270
position = [0,0]


for row in data:
    print(position)
    print(direction)
    print(row)
    position, direction = Movement(position, direction, row)

print('Position:', position)
print('Manhattan distance:', abs(position[0])+abs(position[1]))

        
