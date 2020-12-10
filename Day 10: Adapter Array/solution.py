import os
from collections import defaultdict


def loadInput():
    fileName = "input.txt"
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()

intInputs = list(map(int, inputLines))
sortedIntInputs = sorted(intInputs)


def highest(product=True):
    highest = 0
    one = 0
    three = 1
    for i in range(len(sortedIntInputs)):
        diff = sortedIntInputs[i] - highest
        if(diff <= 3):
            highest = sortedIntInputs[i]
            one += diff == 1
            three += diff == 3
        else:
            break

    if product:
        return one * three
    return highest


def numWayBase():
    wayDict = defaultdict(int)
    wayDict[0] = 1
    for i in sortedIntInputs:
        total = 0
        for j in range(1, 4):
            total += wayDict[i - j]
        wayDict[i] = total

    return wayDict[highest(False)]


print(highest())  # 2516
print(numWayBase())  # 296196766695424
