#!/usr/bin/python3

def AddFrame(matrix):
    rows = len(matrix)
    clns = len(matrix[0])
    zeroRow = ['.']*(clns+2)
    framedMatrix = []
    framedMatrix.append(zeroRow.copy())
    for row in matrix:
        newRow = list('.')
        newRow.extend(row)
        newRow.extend('.')
        framedMatrix.append(newRow)
    framedMatrix.append(zeroRow.copy())
    return framedMatrix

def transMat(matrix):
    occupied = 0
    changes = 0
    framedMatrix = AddFrame(matrix)
    rows = len(matrix)
    cols = len(matrix[0])

    r = 1
    while r < rows + 1:
        c = 1
        while c < cols + 1:
            # above
            tmp =  framedMatrix[r-1][c-1:c+2]
            occNei = tmp.count('#')

            # left and right
            tmp = framedMatrix[r][c-1]
            occNei += tmp.count('#')
            tmp = framedMatrix[r][c+1]
            occNei += tmp.count('#')

            # below
            tmp = framedMatrix[r+1][c-1:c+2]
            occNei += tmp.count('#')

            if framedMatrix[r][c] == 'L' and occNei == 0:
                matrix[r-1][c-1] =  '#'
                changes += 1
            if framedMatrix[r][c] == '#':
                occupied +=1
                if occNei >= 4:
                    matrix[r-1][c-1] =  'L'
                    changes += 1
            c += 1
        r += 1
    return matrix, changes, occupied


with open('input') as f:
#with open('small-input') as f:
    data = [line.rstrip() for line in f]


matrix = []

for row in data:
    matrix.append(list(row))

changes = 1
while changes != 0:
    matrix, changes, occupied = transMat(matrix)

print('Matrix:')
for row in matrix:
    print(row)
print('\n\nOccupied seats:', occupied)
