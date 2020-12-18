import os
import operator


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputs = loadInput()
funcDict = {"+": operator.add, "*": operator.mul}
presDict1 = {"+": 1, "*": 1}
presDict2 = {"+": 2, "*": 1}


def evalExp(exp):
    s = []
    for c in exp:
        if c in funcDict:
            n2 = s.pop()
            n1 = s.pop()
            s.append(funcDict[c](n1, n2))
        else:
            s.append(c)
    return s[0]


def rpn(line, presDict):
    exp = []
    ops = []
    for c in line.replace(" ", ""):
        if(c.isnumeric()):
            exp.append(int(c))
        elif(c in presDict):
            while((not ops == [])):
                top = ops.pop()
                if(not top == "(" and presDict[top] >= presDict[c]):
                    exp.append(top)
                else:
                    ops.append(top)
                    break
            ops.append(c)
        elif(c == "("):
            ops.append(c)
        elif(c == ")"):
            while(not (top := ops.pop()) == "("):
                exp.append(top)
    while(not ops == []):
        exp.append(ops.pop())
    return exp


def evalLine(line, presDict):
    return evalExp(rpn(line, presDict))


def sumInputs(presDict):
    return sum(map(lambda x: evalLine(x, presDict), inputs))


print(sumInputs(presDict1))  # 23507031841020
print(sumInputs(presDict2))  # 218621700997826
