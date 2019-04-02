#!/bin/bash

'''
Aufgabe A3
(c) by Eva Sehr
Inputfiles:
rmHV_10_4 (weight = 13.83)
rmHV_999_4 (weight = 1562.06)
Ausführung: python3 filename.py < inputfile
'''

import sys

inputFile = sys.stdin
nestedList = []
matrixDimension = []
inputFile.readline()

# Gewichte in einer nested List speichern
for row in inputFile.readlines():
    weights = row.strip("  ").strip(" \n").split("   ")
    if (len(weights) > 1):
        # print(weight) #TEST
        rowLength = len(weights)
        nestedList.append(weights)

# Matrix Dimension ermitteln
columnsInDown = len(nestedList[0])
amountSublists = len(nestedList)
rows = len(nestedList[amountSublists - 1]) + 1

# Matrix Initialisierung
countMatrix = {}
for i in range(rows):
    countMatrix[i] = []
    for j in range(columnsInDown):
        countMatrix[i].append(0)

# Erste Reihe nach rechts
for i in range(rows - 1):
    countMatrix[0][i + 1] = round(countMatrix[0][i] + float(nestedList[rows - 1][i]), 2)

# Erste Spalte runter
for i in range(columnsInDown - 1):
    countMatrix[i + 1][0] = round(countMatrix[i][0] + float(nestedList[i][0]), 2)

# Manhattan grid
for j in range(rows - 1):
    for i in range(columnsInDown - 1):
        # runter
        down = round(countMatrix[j][i + 1] + float(nestedList[j][i + 1]), 2)
        # nach rechts
        right = round(countMatrix[j + 1][i] + float(nestedList[rows + j][i]), 2)
        if (down > right):
            countMatrix[j + 1][i + 1] = down
        else:
            countMatrix[j + 1][i + 1] = right

print(countMatrix[rows - 1][columnsInDown - 1])