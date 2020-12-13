#!/usr/bin/python3
import math

with open('input') as f:
#with open('input-small') as f:
    data = [line.rstrip() for line in f]

earliest = int(data[0])
IDs = data[1].split(',')

workingIDs = [int(x) for x in IDs if x != 'x']

#print(workingIDs)

#print(earliest)


winnerDeparture = 100000000000000000000000000000
winnerID        = -1

#print(max(workingIDs))
for id in workingIDs:
    earlierDepart = math.floor(earliest/id) * id
    earliestDepart = earlierDepart + id
#    print(id, earlierDepart, earliestDepart)
    if earliestDepart < winnerDeparture:
        winnerDeparture = earliestDepart
        winnerID = id

print(winnerID, winnerDeparture, winnerID*(winnerDeparture-earliest))
