#!/usr/bin/python3

"""
Aufgabe A5
Needleman-Wunsch Algorithm
Eva M. Sehr
"""

from Bio import SeqIO
from Bio.Seq import Seq
from argparse import ArgumentParser
from Bio.Alphabet import generic_dna
import sys

parser = ArgumentParser()
parser.add_argument('--match', default=1,
                    help='Provide a score for matching nucleotides, default is 1.)')
parser.add_argument('--mismatch', default=-1,
                    help='Provide a score for mismatching nucleotides, default is -1.')
parser.add_argument('--gap', default=-2,
                    help='Provide a score for a gap in the alignment, default is -2.')


args = parser.parse_args()

# Define the input fasta file, coming via stdin
in_seq = SeqIO.parse(sys.stdin, "fasta")

i = 0
for seq in in_seq:
    if i == 0:
        seq1 = seq.seq
        id1 = seq.id
    elif i == 1:
        seq2 = seq.seq
        id2 = seq.id
    else:
        exit("Error: your fasta file contains more than 2 sequences!")
    i += 1

scoringMatrix = [[0]]
pathMatrix = [[" "]]

nrow = len(seq1) + 1
ncol = len(seq2) + 1

# Filling of scoring & path matrix
for i in range(1, ncol, 1):
    scoringMatrix[0].append(scoringMatrix[0][i - 1] + args.gap)
    pathMatrix[0].append("r")

it1 = 0
it2 = 0

for row in range(1, nrow, 1):
    scoringMatrix.append([scoringMatrix[row - 1][0] + args.gap])
    pathMatrix.append(["v"])
    for col in range(1, ncol, 1):
        vertical = scoringMatrix[row - 1][col] + args.gap
        horizontal = scoringMatrix[row][col - 1] + args.gap
        if (seq1[it1] == seq2[it2]):
            diagonal = scoringMatrix[row - 1][col - 1] + args.match
        else:
            diagonal = scoringMatrix[row - 1][col - 1] + args.mismatch

        if horizontal >= vertical and horizontal > diagonal:
            scoringMatrix[row].append(horizontal)
            pathMatrix[row].append("r")
        elif vertical > horizontal and vertical > diagonal:
            scoringMatrix[row].append(vertical)
            pathMatrix[row].append("v")
        elif diagonal >= horizontal and diagonal >= vertical:
            scoringMatrix[row].append(diagonal)
            pathMatrix[row].append("d")
        else:
            exit("Error")
        it2 += 1
    it1 += 1
    it2 = 0

print("The computed similarity score is", scoringMatrix[len(seq1)][len(seq2)], file=sys.stderr)

col = len(pathMatrix[0]) - 1
row = len(pathMatrix) - 1
path = ""

while(row > 0 or col > 0):
    if pathMatrix[row][col] == "d":
        path += "d"
        row -= 1
        col -= 1
    elif pathMatrix[row][col] == "v":
        path += "v"
        row -= 1
    elif pathMatrix[row][col] == "r":
        path += "r"
        col -= 1
    elif pathMatrix[row][col] == " ":
        break
    else:
        print("Error")
path = path[::-1]

alignment = ["","",""]
it1 = 0
it2 = 0
for step in path:
    if step == "d":
        alignment[0] += seq1[it1]
        alignment[1] += seq2[it2]
        if seq1[it1] == seq2[it2]:
            alignment[2] += "*"
        else:
            alignment[2] += " "
        it1 += 1
        it2 += 1
    elif step == "v":
        alignment[0] += seq1[it1]
        alignment[1] += "-"
        alignment[2] += " "
        it1 += 1
    elif step == "r":
        alignment[0] += "-"
        alignment[1] += seq2[it2]
        alignment[2] += " "
        it2 += 1

# Prepare lines of alignment
line1 = SeqIO.SeqRecord(Seq(alignment[0], generic_dna), id1)
line2 = SeqIO.SeqRecord(Seq(alignment[1], generic_dna), id2)
line3 = SeqIO.SeqRecord(Seq(alignment[2]), "")
align = [line1, line2, line3]

# Stdout
SeqIO.write(align, sys.stdout, "clustal")