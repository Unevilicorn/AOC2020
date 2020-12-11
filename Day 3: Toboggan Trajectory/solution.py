from operator import mul
from functools import reduce
import os


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
mapWidth = len(inputLines[0])


def treeCount(slope=(3, 1)):
    (right, down) = slope
    count = 0
    col = 0

    for i in range(0, len(inputLines), down):
        count += inputLines[i][col] == '#'
        col = (col + right) % mapWidth

    return count


def multiplyTree():
    return reduce(mul, map(treeCount, slopes))


print(treeCount())  # 278
print(multiplyTree())  # 9709761600
