testFileName = "actualInput.txt"
testInput = open(testFileName).readlines()

intInput = list(map(int, testInput))

target = 2020


def twoEntry():
    for i in intInput:
        for j in intInput:
            if(i + j == target):
                return(i * j)


def threeEntry():
    for i in intInput:
        for j in intInput:
            for k in intInput:
                if(i + j + k == target):
                    return(i * j * k)


print(twoEntry())
print(threeEntry())
