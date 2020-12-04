import os
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

testFileName = "input.txt"
inputLines = open(os.path.join(__location__, testFileName)).readlines()


def parseLine(line):
    split1 = line.split(' ')

    [num1, num2] = map(int, split1[0].split('-'))
    char = split1[1][:-1]
    pswd = split1[2]
    return (num1, num2, char, pswd)


def checkOccurence(line):
    (minOcc, maxOcc, char, pswd) = parseLine(line)

    occ = pswd.count(char)

    return minOcc <= occ <= maxOcc


def checkPosition(line):
    (pos1, pos2, char, pswd) = parseLine(line)

    def checker(pos):
        if (0 < pos <= len(pswd)):
            return pswd[pos - 1] == char
        else:
            return False

    return checker(pos1) ^ checker(pos2)


def countValid(func):
    return sum(map(func, inputLines))


print(countValid(checkOccurence))  # 398
print(countValid(checkPosition))  # 562
