#!/usr/bin/python3

def SeekOccu(matrix, row, col):
    neigOcc = 0
    rmax = len(matrix) - 1
    cmax = len(matrix[0]) - 1

    # upper left corner
    r = row
    c = col
    while r > 0 and c > 0:
        if matrix[r-1][c-1] == '#':
            neigOcc += 1
            break
        r -= 1
        c -= 1

    # above
    r = row
    c = col
    while r > 1:
        if matrix[r-1][c] == '#':
            neigOcc += 1
            break
        r -= 1

    # upper right
    r = row
    c = col
    while r > 0 and c < cmax - 1:
        if matrix[r-1][c+1] == '#':
            neigOcc += 1
            break
        r -= 1
        c += 1

    # right
    r = row
    c = col
    while c < cmax - 1:
        if matrix[r][c+1] == '#':
            neigOcc += 1
            break
        c += 1

    # lower right
    r = row
    c = col
    while r < rmax - 1 and c < cmax - 1:
        if matrix[r+1][c+1] == '#':
            neigOcc += 1
            break
        r += 1
        c += 1

    # down
    r = row
    c = col
    while r < rmax - 1:
        if matrix[r+1][c] == '#':
            neigOcc += 1
            break
        r += 1

    # lower left
    r = row
    c = col
    while r < rmax - 1 and c > 0:
        if matrix[r+1][c-1] == '#':
            neigOcc += 1
            break
        r += 1
        c -= 1

    # left
    r = row
    c = col
    while c > 0:
        if matrix[r][c-1] == '#':
            neigOcc += 1
            break
        c -= 1
    return neigOcc

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


def transMat2(matrix):
    occupied = 0
    changes = 0
    rows = len(matrix)
    cols = len(matrix[0])
    transMat = []
    r = 0
    while r < rows:
        transRow = matrix[r].copy()
        c = 0
        while c < cols:
            neighOccu = SeekOccu(matrix, r, c)
            if matrix[r][c] == 'L' and neighOccu == 0:
                transRow[c] = '#'
                changes += 1
            if matrix[r][c] == '#':
                occupied += 1
                if neighOccu >= 5:
                    transRow[c] = 'L'
                    changes += 1
            c += 1
        r += 1
        transMat.append(transRow)
    return transMat, changes, occupied


#with open('input') as f:
with open('input-small') as f:
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


###### Part 2

#with open('input') as f:
with open('input-small') as f:
    data = [line.rstrip() for line in f]

matrix = []

for row in data:
    matrix.append(list(row))

changes = 1
#while changes != 0:
matrix, changes, occupied = transMat2(matrix)
matrix, changes, occupied = transMat2(matrix)
print('Matrix:')
for row in matrix:
    print(row)
print('\n\nOccupied seats:', occupied)
