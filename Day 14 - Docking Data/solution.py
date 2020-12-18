import os


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()

parsedInputs = []


def parse():
    for line in inputLines:
        (action, value) = line.split("=")
        if "mask" in action:
            parsedInputs.append(("m", value[1:]))
        else:
            closeBracket = action.find(']')
            memLoc = action[4:closeBracket]
            parsedInputs.append((int(memLoc), int(value)))


def applyMask(value, mask, v1=True):
    binval = list(bin(value)[2:].zfill(36))
    for (i, bit) in enumerate(mask):
        ignoreBit = "X" if v1 else "0"
        if not (bit == ignoreBit):
            binval[i] = bit
    return "".join(binval)


def allPossible(value):
    loc = value.find("X")
    if(loc == -1):
        return ["".join(value)]

    val1 = list(value)
    val1[loc] = 0
    val1 = "".join(map(str, val1))

    val2 = list(value)
    val2[loc] = 1
    val2 = "".join(map(str, val2))

    return allPossible(val1) + allPossible(val2)


def runProgram1():
    out = {}
    currentMask = "X" * 36
    for (loc, value) in parsedInputs:
        if(loc == "m"):
            currentMask = value
        else:
            out[loc] = int(applyMask(value, currentMask), 2)
    return sum(out.values())


def runProgram2():
    allOut = {}
    currentMask = "X" * 36
    for (loc, value) in parsedInputs:
        if(loc == "m"):
            currentMask = value
        else:
            masked = applyMask(loc, currentMask, False)
            for address in allPossible(masked):
                allOut[int(address, 2)] = value

    return sum(allOut.values())


parse()
print(runProgram1())  # 9296748256641
print(runProgram2())  # 4877695371685
