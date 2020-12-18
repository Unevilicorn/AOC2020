import os


def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()


inputLines = loadInput()
earliestTime = int(inputLines[0])
busses = []
pairs = []


def parse():
    busSplit = inputLines[1].split(",")
    for (i, bus) in enumerate(busSplit):
        if not bus == "x":
            ibus = int(bus)
            busses.append(ibus)
            pairs.append((ibus, (ibus - i) % ibus))


def waitTime(n):
    return n - (earliestTime % n)


def gcd(a, b):
    rem = a % b
    if(rem == 0):
        return b
    else:
        return gcd(b, rem)


# from wikipedia
def findInverse(a, n):
    (t1, t2) = (0, 1)
    (r1, r2) = (n, a)
    while not r2 == 0:
        quotient = r1 // r2
        (t1, t2) = (t2, t1 - quotient * t2)
        (r1, r2) = (r2, r1 - quotient * r2)
    if t1 < 0:
        t1 += n
    return t1


def earliestBus():
    minTime = 99999
    bbus = -1
    for bus in busses:
        if(minTime > (time := waitTime(bus))):
            minTime = time
            bbus = bus

    return minTime * bbus


def crt():
    sums = 1
    for (val, _) in pairs:
        sums *= val

    sumList = [sums] * len(pairs)

    for (i, (val, rem)) in enumerate(pairs):
        sumList[i] //= val
        if not sumList[i] % val == rem:
            sumList[i] *= findInverse(sumList[i], val) * rem
    return sum(sumList) % sums


parse()
print(earliestBus())  # 4722
print(crt())  # 825305207525452
