def findRow(boardingPass):
    low = 0
    high = 127
    rowCharacters = boardingPass[:7]
    for position in rowCharacters:
        if position == "F":
            high = (low + high)//2
        elif position == "B":
            low = (low + high)//2 + 1
        else:
            raise Exception("Wrong boarding pass format")
    if low != high:
        raise Exception("ERROR low is not equal to high")

    return low

def findColumn(boardingPass):
    low = 0
    high = 7
    columnCharacters = boardingPass[7:]
    for position in columnCharacters:
        if position == "L":
            high = (low + high)//2
        elif position == "R":
            low = (low + high)//2 + 1
        else:
            raise Exception("Wrong boarding pass format")
    if low != high:
        raise Exception("ERROR low is not equal to high")

    return low

def findSeatID(boardingPass):
    row = findRow(boardingPass)
    column = findColumn(boardingPass)
    seatID = row * 8  + column

    return seatID

with open("input.txt", "r") as fReader:
    boardingPasses = fReader.read().split()
    highestSeatID = 0
try:
    for boardingPass in boardingPasses:
        seatID = findSeatID(boardingPass)
        if seatID > highestSeatID:
            highestSeatID = seatID
except Exception as err:
    print(err)

print("Highest seat ID: " + str(highestSeatID))
