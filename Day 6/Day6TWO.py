with open("input.txt") as fReader:
    groups = fReader.read().split("\n\n")

sumAnswers = 0

for group in groups:
    # print(groups)

    yesCounter = 0
    groupLen = len(group.split("\n"))
    # print("group len: " + str(groupLen))

    #make every answer from group into a single string
    group = group.replace('\n', '')
    
    answersDict = {}
    for answer in group:
        #add letter in dict or increment if it already exists
        answersDict[answer] = answersDict.setdefault(answer, 0) + 1
    # print(answersDict)
    
    for letter in answersDict:
        # print("letter: " + letter, end = " - ")
        # print("num of yes in group: " + str(answersDict[letter]))
        if answersDict[letter] == groupLen:
            yesCounter += 1
            # print("everyone answered " + letter)
    
    sumAnswers += yesCounter
    # print("...")

print("The sum of the counts is " + str(sumAnswers))