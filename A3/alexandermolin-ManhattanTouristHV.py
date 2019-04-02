
import sys

inputFile = sys.stdin
nestedList = []
inputFile.readline()

for row in inputFile.readlines():
    weights = row.strip("  ").strip(" \n").split("   ")
    if (len(weights) > 1):
        rowLength = len(weights)
        nestedList.append(weights)

columnsInDown = len(nestedList[0])
amountSublists = len(nestedList)
rows = len(nestedList[amountSublists - 1]) + 1

countMatrix = {}
for i in range(rows):
    countMatrix[i] = []
    for j in range(columnsInDown):
        countMatrix[i].append(0)

for i in range(rows - 1):
    countMatrix[0][i + 1] = round(countMatrix[0][i] + float(nestedList[rows - 1][i]), 2)

for i in range(columnsInDown - 1):
    countMatrix[i + 1][0] = round(countMatrix[i][0] + float(nestedList[i][0]), 2)

for j in range(rows - 1):
    for i in range(columnsInDown - 1):
        down = round(countMatrix[j][i + 1] + float(nestedList[j][i + 1]), 2)
        right = round(countMatrix[j + 1][i] + float(nestedList[rows + j][i]), 2)
        if (down > right):
            countMatrix[j + 1][i + 1] = down
        else:
            countMatrix[j + 1][i + 1] = right

#Da ich leider gerade beruflich etwas eingespannt bin, werden Sie in diesem Code sehr viele Teile von Kollegen gefunden haben.

print(countMatrix[rows - 1][columnsInDown - 1])

