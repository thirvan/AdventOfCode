with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n")

numGoodPasswords = 0

for line in lines:
    instances = 0
    line = line.split(":")
    policy = line[0]
    password = line[1][1:]
    rangeTimes = policy[:-1].split("-")
    leastTimes = int(rangeTimes[0])
    mostTimes = int(rangeTimes[1])
    letter = policy[-1]

    # print("\npolicy: {}".format(policy))
    # print("rangeTimes: {}".format(rangeTimes))
    # print("leastTimes: {}".format(leastTimes))
    # print("mostTimes: {}".format(mostTimes))
    # print("letter: {}".format(letter))
    # print("password: {}".format(password))

    for character in password:
        if character == letter:
            instances += 1
    if instances >= leastTimes and instances <= mostTimes:
        numGoodPasswords += 1
        # print("GOOD PASSWORD")
    # print("instances of {} in {}: {}".format(letter, password, instances))

print("Number of good passwords: {}".format(numGoodPasswords))


# policies = lines.split(":")
# print(lines)