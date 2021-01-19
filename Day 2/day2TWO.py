with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n")

numGoodPasswords = 0

for line in lines:
    instances = 0
    line = line.split(":")
    policy = line[0]
    password = line[1][1:]
    positions = policy[:-1].split("-")
    firstPosition = int(positions[0])
    secondPosition = int(positions[1])
    letter = policy[-1]

    # print("\npolicy: {}".format(policy))
    # print("positions: {}".format(positions))
    # print("firstPosition: {}".format(firstPosition))
    # print("secondPosition: {}".format(secondPosition))
    # print("letter: {}".format(letter))
    # print("password: {}".format(password))

    firstLetter = password[firstPosition - 1]
    secondLetter = password[secondPosition - 1]

    # print("Letter at first position: {}".format(firstLetter))
    # print("Letter at second position: {}".format(secondLetter))

    if (letter == firstLetter and letter != secondLetter) or (letter != firstLetter and letter == secondLetter):
        numGoodPasswords += 1
        # print("GOOD PASSWORD")

print("Number of good passwords: {}".format(numGoodPasswords))