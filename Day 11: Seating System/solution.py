import os
from pprint import pprint


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()
listInput = list(map(list, inputLines))


def isInrage(table, x, y):
    return x >= 0 and x < len(table[0]) and y >= 0 and y < len(table)


def isFloor(table, x, y):
    return table[y][x] == "."


def isEmpty(table, x, y):
    return table[y][x] == "L"


def isFilled(table, x, y):
    return table[y][x] == "#"


def isEmptyOrFloor(table, x, y):
    return not (isInrage(table, x, y) and isFilled(table, x, y))


def getFilledCount(table, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j == 0:
                total += not isEmptyOrFloor(table, x + i, y + j)
    return total


def getFilledCountFar(table, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j == 0:
                for k in range(1, 999999):
                    newX = x + i * k
                    newY = y + j * k
                    if not isInrage(table, newX, newY):
                        break
                    if not isFloor(table, newX, newY):
                        total += isFilled(table, newX, newY)
                        break

    return total


def evolveOne(table, filledCountFunc=getFilledCountFar,  dieCount=5):
    newTab = []
    for (y, row) in enumerate(table):
        newTab.append([])
        for (x, cell) in enumerate(row):
            if(cell == "."):
                newTab[-1].append(".")
            else:
                filledCount = filledCountFunc(table, x, y)
                if(cell == "L" and filledCount == 0):
                    newTab[-1].append("#")
                elif(cell == "#" and filledCount >= dieCount):
                    newTab[-1].append("L")
                else:
                    newTab[-1].append(cell)
    return newTab


def countChair(table):
    total = 0
    for row in table:
        for cell in row:
            if cell == "#":
                total += 1
    return total


def totalChairWhenStop(filledCountFunc, dieCount):
    prev = listInput
    while not (prev == (curr := evolveOne(prev, filledCountFunc, dieCount))):
        prev = curr
    return countChair(prev)


print(totalChairWhenStop(getFilledCount, 4))  # 2319
print(totalChairWhenStop(getFilledCountFar, 5))  # 2117
