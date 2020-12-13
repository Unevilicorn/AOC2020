import os
from pprint import pprint


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()

(north, east, south, west) = ((0, 1), (1, 0), (0, -1), (-1, 0))

rotDict = {0: east, 90: south, 180: west, 270: north}
vecDict = {"E": east, "S": south, "W": west, "N": north}
dirSign = {"L": -1, "R": 1}


def addVec(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def multVec(v, m):
    return (v[0] * m, v[1] * m)


def addMultVec(v1, v2, m):
    return addVec(v1, multVec(v2, m))


def forward(p, r, n):
    return addMultVec(p, rotDict[r], n)


def relativeForward(p, w, n):
    return addMultVec(p, w, n)


def rotWay(wp, ds, n):
    (wx, wy) = wp
    for _ in range(n // 90):
        (wx, wy) = multVec((wy, -wx), ds)
    return (wx, wy)


def rot(r, n, sign):
    return (r + n * sign) % 360


def manhattonDistance():
    p = (0, 0)
    r = 0
    for line in inputLines:
        d = line[0]
        n = int(line[1:])
        if(d in "F"):
            p = forward(p, r, n)
        elif(d in "LR"):
            r = rot(r, n, dirSign[d])
        else:
            p = addMultVec(p, vecDict[d], n)
    return abs(p[0]) + abs(p[1])


def relativeManhattonDistance():
    p = (0, 0)
    w = (10, 1)
    for line in inputLines:
        d = line[0]
        n = int(line[1:])
        if(d == "F"):
            p = relativeForward(p, w, n)
        elif(d in "LR"):
            w = rotWay(w, dirSign[d], n)
        else:
            w = addMultVec(w, vecDict[d], n)
    return abs(p[0]) + abs(p[1])


print(manhattonDistance())  # 1838
print(relativeManhattonDistance())  # 89936
