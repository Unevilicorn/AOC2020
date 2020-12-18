import os
from collections import defaultdict


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()[0].split(",")


inputs = loadInput()
intInputs = list(map(int, inputs))

target1 = 2020
target2 = 30000000


def addOcc(dic, n, i):
    if(len(dic[n]) == 2):
        dic[n] = [dic[n][1], i]
    else:
        dic[n].append(i)


def findAtTarget(target):
    dic = defaultdict(list)

    for (i, n) in enumerate(intInputs, 1):
        dic[n].append(i)

    last = intInputs[-1]
    for i in range(len(intInputs) + 1, target + 1):
        length = len(dic[last])
        if(length == 1):
            addOcc(dic, 0, i)
            last = 0
        elif(length == 2):
            l = dic[last]
            last = l[1] - l[0]
            addOcc(dic, last, i)
        else:
            print("boroken")
    return last


print(findAtTarget(target1))  # 758
print(findAtTarget(target2))  # 814
