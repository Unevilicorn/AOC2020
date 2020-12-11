import os
from collections import defaultdict


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()
bags = {}
checkedBags = {}


def listToColor(l):
    return "%s %s" % (l[0], l[1])


def parseBags():
    for line in inputLines:
        words = line.split()
        thisColor = listToColor(words[0:2])
        colorAndCount = {}

        if(not words[4] == "no"):
            for i in range(5, len(words), 4):
                colorAndCount[listToColor(words[i:i+2])] = int(words[i-1])

        bags[thisColor] = colorAndCount


def recCheck(color):
    if color == "shiny gold":
        return 1
    elif color in checkedBags:
        return checkedBags[color]
    else:
        s = any(map(recCheck, bags[color]))
        checkedBags[color] = s
        return s


def allPathCount():
    return sum(map(recCheck, bags)) - 1


def recCount(color):
    bagDict = bags[color]
    if(not bagDict):
        return 0
    else:
        total = 0
        for key in bagDict.keys():
            total += (recCount(key) + 1) * bagDict[key]
        return total


def totalBagCount():
    return recCount("shiny gold")


parseBags()
print(allPathCount())  # 222
print(totalBagCount())  # 13264
