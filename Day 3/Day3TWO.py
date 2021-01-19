def calcNumTrees(numRight, numDown, numRows, numCols):
    numSlopes = math.ceil(numRows / numDown)
    gridCols = numSlopes * numRight
    gridRows = numRows
    multipleInputs = math.ceil(gridCols / numCols)
    grid = []
    for row in lines:
        grid.append(row * multipleInputs)
    numTrees = 0
    for i in range(1, numSlopes):
        rightSpace = i * numRight
        downSpace = i * numDown
        # print("right space: " + str(rightSpace))
        # print("down space: " + str(downSpace))
        if rightSpace <= gridCols and downSpace <= gridRows:
            space = grid[downSpace][rightSpace]
            if space == "#":
                numTrees += 1
    print("num trees: " + str(numTrees))
    return numTrees

import math

with open("input.txt", "r") as fReader:
    lines = fReader.read().split("\n")

numRows = len(lines)
numCols = len(lines[0])

numRight = [1, 3, 5, 7, 1]
numDown = [1, 1, 1, 1, 2]

productTrees = 1

for i in range(len(numRight)):
    productTrees *= calcNumTrees(numRight[i], numDown[i], numRows, numCols)

print("Product trees: " + str(productTrees))
