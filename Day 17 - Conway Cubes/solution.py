import os
import operator
from itertools import combinations
from pprint import pprint


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputs = loadInput()
tableInput = list(map(list, inputs))

stayActive = (2, 3)
comeActive = (3,)


def addTuple(t1, t2):
    return tuple(map(operator.add, t1, t2))


def isActive(tab, pos):
    currentTab = tab
    for p in pos:
        if not 0 <= p < len(currentTab):
            return False
        currentTab = currentTab[p]

    return currentTab == "#"


def genNeighbourPos(pos):
    neighbours = []
    if len(pos) > 1:
        (a, *b) = pos
        for slice in range(a - 1, a + 2):
            positions = genNeighbourPos(tuple(b))
            neighbours += [(slice, ) + pos for pos in positions]
    else:
        (a,) = pos
        for i in range(a - 1, a + 2):
            neighbours += [(i,)]
    return neighbours


def neighbourCount(tab, pos):
    neighbours = genNeighbourPos(pos)
    neighbours.remove(pos)

    total = 0
    for position in neighbours:
        total += isActive(tab, position)
    return total


def tabDepthCounter(tab):
    d = 0
    newTab = tab
    while not isinstance(newTab, str):
        d += 1
        newTab = newTab[0]
    return d


def padTab(tab, dim):
    newTab = tab
    depthDiff = dim - tabDepthCounter(tab)
    for _ in range(depthDiff):
        newTab = [newTab]
    return newTab


def getTabShape(tab):
    shape = ()
    temp = tab
    while not isinstance(temp, str):
        shape += (len(temp),)
        temp = temp[0]
    return shape


def getNextCoords(shape):
    coords = []
    if len(shape) > 1:
        (a, *b) = shape
        for slice in range(-1, a + 1):
            positions = getNextCoords(tuple(b))
            coords += [(slice, ) + pos for pos in positions]
    else:
        (a,) = shape
        coords = [(i,) for i in range(-1, a + 1)]
    return coords


def createTable(shape):
    tab = []
    if len(shape) > 1:
        (a, *b) = shape
        for _ in range(a):
            positions = createTable(b)
            tab.append([pos for pos in positions])
    else:
        (a,) = shape
        tab = ["." for i in range(a)]
    return tab


def setActive(tab, pos):
    newPos = pos
    newTab = tab
    while len(newPos) > 1:
        (a, *b) = newPos
        newTab = newTab[a]
        newPos = tuple(b)
    (index, ) = newPos
    newTab[index] = "#"


def getActiveCount(tab):
    total = 0
    if(isinstance(tab, str)):
        return tab == "#"
    for slice in tab:
        total += getActiveCount(slice)
    return total


def evolveOne(tab, dim):
    shape = getTabShape(tab)
    coords = getNextCoords(shape)

    newShape = addTuple(shape, (2,) * dim)
    newTab = createTable(newShape)
    for coord in coords:
        count = neighbourCount(tab, coord)
        active = isActive(tab, coord)
        stayAlive = count in stayActive and active
        comeAlive = count in comeActive and not active
        if(comeAlive or stayAlive):
            setActive(newTab, addTuple(coord, (1,) * dim))

    return newTab


def solve(dim, times):
    paddedTab = padTab(tableInput, dim)
    outTab = paddedTab
    for _ in range(times):
        outTab = evolveOne(outTab, dim)
    return getActiveCount(outTab)


pprint(solve(3, 6))  # 386
pprint(solve(4, 6))  # 2276
