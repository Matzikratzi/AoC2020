#!/usr/bin/python3
import re

# Function that reads the input file and initiates the cards for the
# players
def Dealer():
    with open('input') as f:
    # with open('input-smallest') as f:
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

# Function that decides the winnig card each part 1 round
def Combat(c1, c2):
    if c1 > c2:
        winner = 1
    else:
        winner = 2
        
    return winner

def Part1():
    cardsP1, cardsP2 = Dealer()
    print('P1: ', cardsP1)
    print('P2: ', cardsP2)

    gameOver = False

    while cardsP1 != [] and cardsP2 != []:
        c1 = cardsP1.pop(0)
        c2 = cardsP2.pop(0)
        winner = Combat(c1, c2)
        if winner == 1:
            cardsP1.append(c1)
            cardsP1.append(c2)
        else:
            cardsP2.append(c2)
            cardsP2.append(c1)
    
    # print('P1: ', cardsP1)
    # print('P2: ', cardsP2)

    if cardsP1 == []:
        winningHand = cardsP2
    else:
        winningHand = cardsP1
        
    points = 0
    i = 0
    iMax = len(winningHand)
    while i < iMax:
        points += winningHand[i]*(iMax-i)
        i += 1

    print('Part 1 Winning Score:', points)

# Part1()
game = 1

def GameIsPlayed(d1, d2, previousDecks):
    # print(playedGames)
    for game in previousDecks:
        oldD1 = game[0]
        oldD2 = game[1]
        if d1 == oldD1 and d2 == oldD2:
            return True, previousDecks

    previousDecks.append([d1.copy(), d2.copy()])
    return False, previousDecks

# Function that decides the winnig card each part 1 round
def RecCombat(d1, d2, gameNum):
    global game
    previousDecks = []
    runda = 1
    runBefore = False
    while True:
        if d1 == []:
            # print('The winner of game', gameNum, 'is player', 2)
            return 2, d2
        elif d2 == []:
            # print('The winner of game', gameNum, 'is player', 1)
            return 1, d1
        else:
            # print('-- Round', runda, '(Game', gameNum,') --')
            # print('Player 1\'s deck:', d1)
            # print('Player 2\'s deck:', d2)
            again, previousDecks = GameIsPlayed(d1, d2, previousDecks)
            if again:
                print('Same game again!')
                print('The winner of game', gameNum, 'is player', 1)
                print('deck 1:', d1)
                points = 0
                i = 0
                iMax = len(d1)
                while i < iMax:
                    points += d1[i]*(iMax-i)
                    i += 1
                print('Part 2 Winning Score:', points)

                return 1, d1, True
            else:
                c1 = d1.pop(0)
                c2 = d2.pop(0)
                # print('Player 1 plays:', c1)
                # print('Player 2 plays:', c2)

                if c1 <= len(d1) and c2 <= len(d2):
                    # recursive!
                    # print('Playing a sub-game to determine the winner.')
                    game += 1
                    winner = RecCombat(d1[:c1], d2[:c2], game-1)
                    # print('\n...anyway, back to game', gameNum)
                else:
                    if c1 > c2:
                        winner = 1
                    else:
                        winner = 2
                        
        if winner == 1:
            # print('Player 1 wins round', runda,' of game,', gameNum)
            d1.extend([c1, c2])
        else:
            # print('Player 2 wins round', runda,' of game,', gameNum)
            d2.extend([c2, c1])
        runda += 1

def Part2():
    global game
    cardsP1, cardsP2 = Dealer()
    print('P1: ', cardsP1)
    print('P2: ', cardsP2)
    game += 1
    winner, deck = RecCombat(cardsP1, cardsP2, game-1)

    points = 0
    i = 0
    iMax = len(deck)
    while i < iMax:
        points += deck[i]*(iMax-i)
        i += 1

    print('Part 2 Winning Score:', points)
    print('Winner:', winner)
    print('Deck:', deck)
Part2()
