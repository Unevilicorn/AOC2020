import os
from collections import defaultdict


def loadInput():
    fileName = "input.txt"
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()

lookUpTable = {"B": 1, "F": 0, "L": 0, "R": 1}


def seatID(codeStr):
    total = 0
    for i, c in enumerate(reversed(codeStr)):
        total += lookUpTable[c] * 1 << i

    return total


def maxID():
    return max(map(seatID, inputLines))


def misingID():
    possibleSeats = defaultdict(int)
    seats = map(seatID, inputLines)
    seats = filter(lambda seat: (8 <= seat <= 1015), seats)

    for seat in seats:
        possibleSeats[seat] += 2
        possibleSeats[seat - 1] += 1
        possibleSeats[seat + 1] += 1

    for seat in possibleSeats:
        if possibleSeats[seat] == 2:
            return seat


print(maxID())  # 888
print(misingID())  # 522
