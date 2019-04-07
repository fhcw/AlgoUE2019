
import sys

matrix = sys.stdin.readlines()
matrix_liste = list()

for line in matrix:
    matrix_liste.append(line.strip().split())

del matrix_liste[0]

matrix_laenge = len(matrix_liste[0])
del matrix_liste[matrix_laenge -1]
del matrix_liste[matrix_laenge -1]
del matrix_liste[matrix_laenge*2 - 1]
del matrix_liste[matrix_laenge*2 - 1]

mht_matrix = [[0] * matrix_laenge for i in range(matrix_laenge)]

for rechts in range(matrix_laenge - 1):
    mht_matrix[0][rechts + 1] = round(mht_matrix[0][rechts] + float(matrix_liste[matrix_laenge-1][rechts]), 2)

for down in range(matrix_laenge - 1):
    mht_matrix[down+1][0] = round(mht_matrix[down][0] + float(matrix_liste[down][0]), 2)

for j in range(matrix_laenge - 1):
    for i in range(matrix_laenge - 1):
        down = round(mht_matrix[j][i+1] + float(matrix_liste[j][i+1]), 2)
        rechts = round(mht_matrix[j+1][i] + float(matrix_liste[matrix_laenge + j][i]), 2)
        diagonal = round(mht_matrix[j][i] + float(matrix_liste[matrix_laenge*2 -1 + j][i]), 2)
        mht_matrix[j+1][i+1] = max(down, rechts, diagonal)
       

print (mht_matrix[matrix_laenge-1][matrix_laenge-1])


