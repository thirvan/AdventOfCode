from typing import ValuesView


def validatePassport(keys, values):
    requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]
    valid = True
    for requiredKey in requiredKeys:
        # print(requiredKey)
        try:
            keyIndex = keys.index(requiredKey)
            print("{}: {} index: {}".format(requiredKey,values[keyIndex], keyIndex))
        except ValueError:
            valid = False
    
    return valid

def validatebyr(value):
    valid = True
    try:
        value = int(value)
        if value < 1920 or value > 2002:
            valid = False
    except ValueError:
        valid = False

    return valid

def validateiyr(value):
    valid = True
    try:
        value = int(value)
        if value < 2010 or value > 2020:
            valid = False
    except ValueError:
        valid = False

    return valid

def validateeyr(value):
    valid = True
    try:
        value = int(value)
        if value < 2020 or value > 2030:
            valid = False
    except ValueError:
        valid = False

    return valid

def validatehgt(value):
    valid = True
    number = value[:-2]
    unit = value[-2:]
    try:
        if unit != "cm" and unit != "in":
            raise ValueError
        number = int(number)
        if unit == "cm" and number < 150 or number > 193:
            valid = False
        if unit == "in" and number < 59 or number > 76:
            valid = False
    except ValueError:
        valid = False

    return valid

def validatehcl(value):
    valid = True
    hex = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", 
    "d", "e", "f"}
    try:
        if value[0] != "#":
            raise ValueError
        if len(value) != 7:
            raise ValueError
        for character in value[1:]:
            if character not in hex:
                raise ValueError
    except ValueError:
        valid = False
    
    return valid

with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n\n")

def validateecl(value):
    valid = True
    validEyeColors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if value not in validEyeColors:
        valid = False
    
    return valid

def validatepid(value):
    valid = True

    try:
        if len(value) != 9:
            valid = False
        value = int(value)
    except ValueError:
        valid = False

    return valid

validPassports = 0

for i, line in enumerate(lines):
    fields = []
    keys = []
    values = []
    lineFields = line.split("\n")
    for lineField in lineFields:
        field = lineField.split(" ")
        for f in field:
            fields.append(f)
            keys.append(f[:3])
            values.append(f[4:])
    # print("\n----" + str(i) + ":\n")
    # print(fields)
    # print(keys)
    if validatePassport(keys, values):
        validPassports += 1
print("valid passports: " + str(validPassports) )
# print(lines)

value = "2022"
print("byr {} is {}".format(value, validatebyr(value)))
print("iyr {} is {}".format(value, validateiyr(value)))
print("eyr {} is {}".format(value, validateeyr(value)))
height = "77in"
print("hgt {} is {}".format(height, validatehgt(height)))

haircolor = "#43cdea"
print("hcl {} is {}".format(haircolor, validatehcl(haircolor)))

eyecolor = "grn"
print("ecl {} is {}".format(eyecolor, validateecl(eyecolor)))

passportID = "245532345"
print("pid {} is {}".format(passportID, validatepid(passportID)))
