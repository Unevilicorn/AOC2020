import os


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()

intInputs = list(map(int, inputLines))
length = len(inputLines)

firstX = 25


def twoEntryHash(target, inputs):
    h = {}
    for i in inputs:
        if i in h:
            return True
        else:
            h[target - i] = 0
    return False


def findInvalid():
    for i in range(firstX, length):
        if(not twoEntryHash(intInputs[i], intInputs[i - firstX: i])):
            return intInputs[i]


def findSumToInvalid():
    invalidNum = findInvalid()

    pointer1 = 0
    pointer2 = 1
    sums = intInputs[0] + intInputs[1]
    while(sums != invalidNum):
        if(sums < invalidNum or (pointer2 - pointer1) == 0):
            pointer2 += 1
            sums += intInputs[pointer2]
        else:
            sums -= intInputs[pointer1]
            pointer1 += 1

    sumRange = intInputs[pointer1: pointer2 + 1]
    return min(sumRange) + max(sumRange)


print(findInvalid())  # 105950735
print(findSumToInvalid())  # 13826915
