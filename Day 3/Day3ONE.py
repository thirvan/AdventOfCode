import math

with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n")

numRows = len(lines)
numCols = len(lines[0])
numRight = 3
numDown = 1
numSlopes = math.ceil(numRows / numDown)
gridCols = numSlopes * numRight
gridRows = numRows
multipleInputs = math.ceil(gridCols / numCols)
grid = []
numTrees = 0

for row in lines:
    grid.append(row * multipleInputs)

for i in range(1, numSlopes):
    rightSpace = i * numRight
    downSpace = i * numDown
    # print("right space: " + str(rightSpace))
    # print("down space: " + str(downSpace))
    if rightSpace <= gridCols and downSpace <= gridRows:
        space = grid[downSpace][rightSpace]
        if space == "#":
            numTrees += 1
        # print(space)

# print("num rows: " + str(numRows))
# print("num cols: " + str(numCols))
# print("num Slopes: " + str(numSlopes))
# print("grip cols: " + str(gridCols))
# print("grip rows: " + str(gridRows))
print("num trees: " + str(numTrees))

# print(lines)
