#!/usr/bin/python3
import re

def Dealer():
    with open('input') as f:
    #with open('input-small') as f:
        data = [line.rstrip() for line in f]

    hP1 = []
    hP2 = []
    currentHand = hP1

    for row in data:
        if row == 'Player 1:':
            currentHand = hP1
        elif row == 'Player 2:':
            currentHand = hP2
        elif re.match(r"[0-9]+", row):
            currentHand.append(int(row))
    return hP1, hP2


def round(hP1, hP2):
    gameOver = False
    if hP1 !=[] and hP2 != []:
        cP1 = hP1.pop(0)
        cP2 = hP2.pop(0)
        if cP1 > cP2:
            hP1.extend([cP1, cP2])
        else:
            hP2.extend([cP2, cP1])
    else:
        gameOver = True
        
    return gameOver, hP1, hP2

cardsP1, cardsP2 = Dealer()
print('P1: ', cardsP1)
print('P2: ', cardsP2)

gameOver = False

while(gameOver == False):
    gameOver, cardsP1, cardsP2 = round(cardsP1, cardsP2)
    
print('P1: ', cardsP1)
print('P2: ', cardsP2)

if cardsP1 == []:
    winningHand = cardsP2
else:
    winningHand = cardsP1
    
points = 0
i = 0
iMax = len(winningHand)
while i < iMax:
    print(winningHand[i], iMax-i)
    points += winningHand[i]*(iMax-i)
    i += 1

print('Winning Score:', points)
