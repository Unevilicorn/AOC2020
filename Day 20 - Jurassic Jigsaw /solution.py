import os
from pprint import pprint


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().split("\n\n")


inputs = loadInput()
tileDict = {}
edgeOccurDict = {}
visited = {}
assembled = []

direction = {0: (0, -1), 1: (1, 0), 2: (0, -1), 3: (1, 0)}
flipXDict = {0: 4, 1: 3, 2: 6, 3: 1, 4: 0, 5: 7, 6: 2, 7: 5}
flipYDict = {0: 2, 1: 5, 2: 0, 3: 7, 4: 6, 5: 1, 6: 4, 7: 3}
mirror = {0: 2, 2: 0, 1: 3, 3: 1}


def addTuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def splitEdges(tile):
    left = ""
    right = ""
    core = []

    for line in tile[1:-1]:
        core.append(line[1:-1])

    for line in tile:
        left += line[0]
        right += line[-1]

    edges = [tile[0], right, tile[-1], left]
    edges += list(map(lambda x: x[::-1], edges))

    return (edges, core)


def parseInputs():
    for tile in inputs:
        splitTile = tile.split("\n")
        tn = int(splitTile[0][5:9])
        (edges, core) = splitEdges(splitTile[1:])
        tileDict[tn] = {"core": core, "edges": edges}
        for (i, edge) in enumerate(edges):
            if(edge in edgeOccurDict):
                edgeOccurDict[edge]["occ"] += 1
                edgeOccurDict[edge]["ids"][tn] = i
            else:
                edgeOccurDict[edge] = {"occ": 1, "ids": {tn: i}}


def findNotTile(edge, notTile):
    for tile in edgeOccurDict[edge]["ids"]:
        if(not tile == notTile):
            return (tile, edgeOccurDict[edge]["ids"][tile])


def flipX(tile):
    tileDict[tile]["core"] = list(
        map(lambda x: x[::-1], tileDict[tile]["core"]))
    edges = tileDict[tile]["edges"][::]
    for i in range(8):
        newi = flipXDict[i]
        tileDict[tile]["edges"][i] = edges[newi]
        edgeOccurDict[edges[newi]]["ids"][tile] = newi


def flipY(tile):
    tileDict[tile]["core"] = tileDict[tile]["core"][::-1]
    edges = tileDict[tile]["edges"][::]
    for i in range(8):
        newi = flipYDict[i]
        tileDict[tile]["edges"][i] = edges[newi]
        edgeOccurDict[edges[newi]]["ids"][tile] = newi


def combineTile(tile):
    edges = tileDict[tile]["edges"]
    core = [edges[0]] + tileDict[tile]["core"][::] + [edges[2]]
    for i in range(1, len(core) - 1):
        core[i] = edges[3][i] + core[i] + edges[1][i]
    return core


def getNewij(i, j, size):
    mid = (size - 1) / 2
    (newi, newj) = addTuple((i, j), (-mid,) * 2)
    (newi, newj) = (-newj, newi)
    (newi, newj) = addTuple((newi, newj), (mid,) * 2)
    return (int(newi), int(newj))


def rotate(tile):
    combinedTile = combineTile(tile)

    lcore = len(combinedTile)
    newTile = ["" * lcore] * lcore
    for i in range(lcore):
        for j in range(lcore):
            (newi, newj) = getNewij(i, j, lcore)
            newTile[i] += combinedTile[newi][newj]

    (edges, newCore) = splitEdges(newTile)
    tileDict[tile]["edges"] = edges
    tileDict[tile]["core"] = newCore
    for i in range(8):
        edgeOccurDict[edges[i]]["ids"][tile] = i


def transform(tile, facing, toFace):
    print(f"trasforming {tile} {facing} {toFace}")
    if(facing == toFace):
        return
    newFacing = facing

    if newFacing in (4, 6):
        flipX(tile)
        newFacing = flipXDict[facing]
    elif newFacing in (5, 7):
        flipY(tile)
        newFacing = flipYDict[facing]
    print(f"after flip {tile} {newFacing} {toFace}")
    for _ in range((toFace - newFacing) % 4):
        rotate(tile)
        newFacing = (newFacing + 1) % 4
    print(f"after rot {tile} {newFacing} {toFace}")


def recFind(tile, pos):
    if(tile in visited):
        return

    visited[tile] = 1
    print()
    print(pos[0], pos[1], tile)
    assembled[pos[0]][pos[1]] = tile  # tileDict[tile]["core"]
    for i in range(4):
        edge = tileDict[tile]["edges"][i]
        if edgeOccurDict[edge]["occ"] == 2:
            (otherTile, facing) = findNotTile(edge, tile)
            if not otherTile in visited:
                newPos = addTuple(pos, direction[i])
                toFace = mirror[i]
                print(tile, otherTile, i, facing, newPos)
                transform(otherTile, facing, toFace)
                recFind(otherTile, newPos)


def assemble():
    size = int(len(inputs) ** 0.5)
    extraSize = size * 2 - 1
    for _ in range(extraSize):
        assembled.append([])
        for _ in range(extraSize):
            assembled[-1].append("00")
    recFind(1951, (size - 1, size - 1))
    # recFind(1301, (size, size))


def part1():
    total = 1
    for tile in tileDict:
        outEdgeCount = 0
        for edge in tileDict[tile]["edges"][: 4]:
            if edgeOccurDict[edge]["occ"] == 1:
                outEdgeCount += 1
        if(outEdgeCount == 2):
            total *= tile
    return total


def part2():

    return assembled


parseInputs()
# assemble()
# print(edgeOccurDict)
# pprint(assembled)
print(part1())  # 8272903687921
# print(part2())  # 8272903687921

# pprint(combineTile(1171))
# transform(1171, 5, 3)
# pprint(combineTile(1171))

# print()

# pprint(combineTile(1171))
# flipY(1171)
# pprint(combineTile(1171))
# rotate(1171)
# pprint(combineTile(1171))
# rotate(1171)
# pprint(combineTile(1171))
