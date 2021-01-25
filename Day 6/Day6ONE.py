with open("input.txt") as fReader:
    groups = fReader.read().split("\n\n")

sumAnswers = 0

for group in groups:
    group = group.replace('\n', '')
    answers = set()
    for answer in group:
        answers.add(answer)
    # print(answers)
    sumAnswers += len(answers)

print("The sum of the counts is " + str(sumAnswers))