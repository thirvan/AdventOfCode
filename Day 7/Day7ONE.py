from ruleClass import Rule

with open("input.txt") as fReader:
    lines = fReader.read().split("\n")

# rules = []
for line in lines:
    rule = Rule(line)
    # print(rule  )
    
    
    # rule = []
    # # print(line)
    # temp = line.split(" bags contain ")
    # rule.append(temp[0])
    
    # tempList = temp[1].split(", ")

    # for content in tempList:
    #     rule.append(content)
    #     print(content[0])

    # # rule.extend(tempList)
    # rule[-1] = rule[-1][:-1]
    # print(rule)
    # print(rule)
    # rules.append(rule)

# for rule in rules:
#     print(rule)