print("Hello World")

with open("input.txt", "r") as inputFile:
    file = inputFile.read()

numbers = file.split("\n")

for i,number in enumerate(numbers):
    entryOne = int(numbers[i])
    #print(entryOne)

    for j in range(i + 1, len(numbers)):
        entryTwo = int(numbers[j])
        sum = entryOne + entryTwo
        #print("{0} + {1} = {2}".format(entryOne, entryTwo, sum))
        if sum == 2020:
            print("entryOne: {} + entryTwo: {}".format(entryOne, entryTwo))
            print("answer = {}".format(entryOne * entryTwo))
