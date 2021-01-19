from typing import ValuesView


def validatePassport(keys):
    requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]
    valid = True
    for requiredKey in requiredKeys:
        # print(requiredKey)
        try:
            keyIndex = keys.index(requiredKey)
            # print("index of {}: {}", requiredKey, keyIndex)
        except ValueError:
            valid = False
    
    return valid

with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n\n")

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
    if validatePassport(keys):
        validPassports += 1
print("valid passports: " + str(validPassports) )
# print(lines)
