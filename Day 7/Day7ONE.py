with open("input.txt") as fReader:
    lines = fReader.read().split("\n")

for line in lines:
    rule = []
    print(line)
    temp = line.split(" bags contain ")
    rule.append(temp[0])
    rule.extend(temp[1].split(", "))
    print(rule)