#!/usr/bin/python3

import sys
from math import sqrt

def Main():
    down = downValues()
    right = rightValues()

    if (down == "invalid" or right == "invalid"):
        print("Input invalid. Program aborted!")
        return 100

    matrix = [[0 for x in range(len(right))] for y in range(len(right))] 

    fillFirstRow(matrix, right)
    fillFirstCol(matrix, down)

    for i, v in enumerate(matrix):
        print(matrix[i])

    print("Down")
    print(len(down), "x", (len(down[0])))
    print("Right")
    print(len(right), "x", (len(right[0])))


def downValues():
    dValues = []

    for line in sys.stdin:
        if (line[0] == 'G'):
            continue
        line = line.strip()
        if (line == "---"):
            break
        temp = line.rsplit("   ")
        for i, v in enumerate(temp):
            temp[i] = float(temp[i])
        dValues.append(temp)
    
    dValues_len = len(dValues)

    # Check if (N-1) * N is given
    for i, v in enumerate(dValues):
        if (len(dValues[i]) != dValues_len + 1):
            return "invalid"

    return dValues

def rightValues():
    rValues = []

    for line in sys.stdin:
        if (line[0] == 'G'):
            continue
        line = line.strip()
        if (line == "---"):
            #temp.clear()
            continue
        temp = line.rsplit("   ")
        for i, v in enumerate(temp):
            temp[i] = float(temp[i])
        rValues.append(temp)

    rValues_len = len(rValues)

    # Check if N * (N-1) is given
    for i, v in enumerate(rValues):
        if (len(rValues[i]) + 1 != rValues_len):
            return "invalid"

    return rValues

def fillFirstRow(matrix, right):
    matrix[0][1] = matrix[0][0] + right[0][0]
    
    for i in range(2,len(matrix[0])):
        matrix[0][i] = matrix[0][i-1] + right[0][i-1]

def fillFirstCol(matrix, down):
    matrix[1][0] = matrix[0][0] + down[0][0]

    for i in range(2, len(matrix)):
        matrix[i][0] = matrix[i-1][0] + down[i-1][0]

if __name__ == "__main__":
    Main()