with open("input.txt") as fReader:
    rules = fReader.read().split("\n")

for rule in rules:
    print(rule)