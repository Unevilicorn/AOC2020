import os
from collections import Counter


def loadInput():
    fileName = "input.txt"
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read()


inputLines = loadInput().split("\n\n")


def yesCount():
    total = 0
    for line in inputLines:
        total += len(Counter(line + "\n")) - 1
    return total


def allYes():
    total = 0
    for line in inputLines:
        numppl = line.count("\n") + 1
        vals = (Counter(line + "\n").values())
        total += len([c for c in vals if c == numppl]) - 1
    return total


print(yesCount())  # 6335
print(allYes())  # 3392
