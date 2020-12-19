import os
import operator

def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().split("\n\n")


inputs = loadInput()
words = inputs[1].split("\n")
rules = {}
validWords = {}


def extractRule(rule):
    (n, rs) = rule.split(": ")
    rs = rs.split(" | ")
    rs = list(map(lambda x : x.split(" "), rs))
    if(rs[0][0].isnumeric()):
        rs = list(map(lambda x: list(map(int, x)), rs))
    else:
        rs[0] = rs[0][0][1]
    return (int(n), rs)

def findRule(rule):
    if "a" in rules[rule][0] or "b" in rules[rule][0]:
        return

    crules = rules[rule]
    out = []
    for rs in crules:
        ss = [""]
        for r in rs:
            findRule(r)
            ss = [s + x for s in ss for x in rules[r]]
        out += ss
    rules[rule] = out

def parseRules():    
    rulesText = inputs[0].split("\n")
    for rule in rulesText:
        (rn, rs) = extractRule(rule)
        rules[rn] = rs

    findRule(0)

    for valids in rules.values():
        for valid in valids:
            validWords[valid] = 1

def rule0Pattern(word):
    fc = rules[42]
    bc = rules[31]
    lfc = len(fc[0])
    lbc = len(bc[0])
    lw = len(word)

    i = 0
    while i <= lw - lfc and word[i : i + lfc] in fc:
        i += lfc
    c1 = i // lfc

    while i <= lw - lbc and word[i : i + lbc] in bc:
        i += lbc
    c2 = (i - c1 * lfc) // lbc

    return i == lw and c1 > c2 > 0

def countCorrect():
    total = 0
    for word in words:
            total += word in validWords
    return total

def countLoopyCorrect():
    total = 0
    for word in words:
        if word in validWords or rule0Pattern(word):
            total += 1
    return total         

parseRules()
print(countCorrect()) # 182
print(countLoopyCorrect()) # not 337
