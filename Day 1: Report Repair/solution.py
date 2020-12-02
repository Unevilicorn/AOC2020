import os

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

testFileName = "inputs.txt"
testInput = open(os.path.join(__location__, testFileName)).readlines()

intInput = list(map(int, testInput))

finalTarget = 2020


def twoEntry(target=finalTarget, inputs=intInput):
    for n1 in inputs[:-1]:
        for n2 in inputs[1:]:
            if(n1 + n2 == target):
                return(n1 * n2)


def threeEntry(target=finalTarget, inputs=intInput):
    for i, n1 in enumerate(inputs[:-2]):
        r = target - n1
        tr = twoEntry(r, inputs[i:])
        if (tr):
            return tr * n1


def twoEntryHash(target=finalTarget, inputs=intInput):
    h = {}
    for i in inputs:
        r = target - i
        if i in h:
            return i * r
        else:
            h[r] = 0


def threeEntryHash(target=finalTarget, inputs=intInput):
    for i, n1 in enumerate(inputs[:-2]):
        r = target - n1
        tr = twoEntryHash(r, inputs[i:])
        if (tr):
            return tr * n1


print(twoEntry())
print(twoEntryHash())
print(threeEntry())
print(threeEntryHash())
