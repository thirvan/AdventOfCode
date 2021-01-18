print("Hello World")

with open("input.txt", "r") as inputFile:
    file = inputFile.read()

numbers = file.split("\n")

for i,number in enumerate(numbers):
    entryOne = int(numbers[i])
    #print(entryOne)

    for j in range(i + 1, len(numbers)):
        entryTwo = int(numbers[j])
    
        for k in range(j + 1, len(numbers)):
            entryThree = int(numbers[k])
            sum = entryOne + entryTwo + entryThree
            if sum == 2020:
                print("entryOne: {} + entryTwo: {} + entryThree: {}".format(entryOne, entryTwo, entryThree))
                print("answer = {}".format(entryOne * entryTwo * entryThree))
