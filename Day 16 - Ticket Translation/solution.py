import os
from collections import defaultdict


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().split("\n\n")


inputs = loadInput()

parsedInputs = {}


def parse():
    splitInpput = [i.split("\n") for i in inputs]
    fields = {}
    for line in splitInpput[0]:
        (key, vals) = line.split(":")
        unpack = vals.split("or")
        fields[key] = []
        for range in unpack:
            (b, e) = map(int, range.split("-"))
            fields[key].append((b, e))
    parsedInputs["fields"] = fields

    parsedInputs["mine"] = list(map(int, splitInpput[1][1].split(",")))

    parsedInputs["near"] = []
    for line in splitInpput[2][1:]:
        parsedInputs["near"] += [list(map(int, line.split(",")))]


def inrange(v, rt):
    (mi, ma) = rt
    return mi <= v <= ma


def scanningErrorRate(v2=True):
    i = 0
    total = 0
    for ticket in [t for t in parsedInputs["near"]]:
        for num in ticket:
            isInrange = False
            for fields in parsedInputs["fields"].values():
                for field in fields:
                    if inrange(num, field):
                        isInrange = True
                        break
            if not isInrange:
                total += num
                if(v2):
                    parsedInputs["near"].pop(i)
                    i -= 1
                    break
        i += 1
    return total


def findOrder():
    order = {}
    fields = parsedInputs["fields"]
    nears = parsedInputs["near"]
    for field in fields:
        order[field] = [i for i in range(len(fields))]

    for ticket in nears:
        for (i, num) in enumerate(ticket):
            for field in fields:
                bowo = False
                for r in fields[field]:
                    if inrange(num, r):
                        bowo = True
                        break
                if(not bowo and i in order[field]):
                    order[field].remove(i)

    while True:
        a = True
        for field in order:
            if len(order[field]) == 1:
                f = order[field][0]
                for field2 in order:
                    if field != field2 and f in order[field2]:
                        order[field2].remove(f)
            else:
                a = False
        if a:
            break

    return {k: order[k][0] for k in order}


def part2():
    order = findOrder()
    a = 1
    for field in order:
        if("departure" in field):
            a *= parsedInputs["mine"][order[field]]

    return a


parse()
print(scanningErrorRate())  # 26941
print(part2())  # 634796407951
