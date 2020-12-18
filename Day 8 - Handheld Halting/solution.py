import os
from collections import defaultdict


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()


def nop(index, num, accum):
    return (index + 1, accum)


def acc(index, num, accum):
    return (index + 1, accum + num)


def jmp(index, num, accum):
    return (index + num, accum)


commandmap = {"nop": nop, "acc": acc, "jmp": jmp}
commands = []


def parseInputs():
    for line in inputLines:
        pair = line.split()
        commands.append((commandmap[pair[0]], int(pair[1])))


def findAccum(unLoop=False):
    index = 0
    accum = 0
    beenBefore = {}
    commandLen = len(commands)
    while(index < commandLen):
        beenBefore[index] = True
        (command, param) = commands[index]
        (index, accum) = command(index, param, accum)
        if(index in beenBefore):
            if unLoop:
                return False
            else:
                return accum
    return accum


def fixLoopFindAccum():
    for index in reversed(range(len(commands))):
        (command, param) = commands[index]
        swap = {jmp: nop, nop: jmp}
        if(command in (nop, jmp)):
            commands[index] = (swap[command], param)
        if(res := findAccum(True)):
            return res
        commands[index] = (command, param)


parseInputs()
print(findAccum())  # 1797
print(fixLoopFindAccum())  # 1036
