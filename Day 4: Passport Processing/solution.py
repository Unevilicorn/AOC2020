import os


def loadInput(fileName):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read()


testfileName = "input.txt"
inputLines = loadInput(testfileName).splitlines() + [""]


requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
hexChar = "0123456789abcdef"
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validateRange(num, mi, ma):
    return mi <= int(num) <= ma


def validateBirthYear(year):
    return validateRange(year, 1920, 2002)


def validateIssueYear(year):
    return validateRange(year, 2010, 2020)


def validateExpirationYear(year):
    return validateRange(year, 2020, 2030)


def validateHeight(height):
    if(len(height) <= 3):
        return False

    unit = height[-2:]
    num = height[:-2]

    if(height[-2:] == "cm"):
        return validateRange(num, 150, 193)
    elif (unit == "in"):
        return validateRange(num, 59, 76)
    else:
        return False


def validateHairColor(color):
    if not (len(color) == 7 and color[0] == '#'):
        return False
    return all(char in hexChar for char in color[1:])


def validateEyeColor(color):
    return color in eyeColors


def validatePassportID(pid):
    return len(pid) == 9 and pid.isnumeric()


def validateFields(passport):
    return (validateBirthYear(passport["byr"]) and
            validateIssueYear(passport["iyr"]) and
            validateExpirationYear(passport["eyr"]) and
            validateHeight(passport["hgt"]) and
            validateHairColor(passport["hcl"]) and
            validateEyeColor(passport["ecl"]) and
            validatePassportID(passport["pid"])
            )


def validatePassport(validateFunction):
    passport = {}
    validCount = 0
    for line in inputLines:
        if(not line == ""):
            lineSplit = map(lambda x: x.split(':'), line.split(' '))
            for splitLine in lineSplit:
                passport[splitLine[0]] = splitLine[1]
        else:
            if all(field in passport for field in requiredFields):
                if not validateFunction or validateFunction(passport):
                    validCount += 1
            passport = {}

    return validCount


print(validatePassport(None))  # 245
print(validatePassport(validateFields))  # 133
