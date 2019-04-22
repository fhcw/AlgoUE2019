import argparse
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(description="Needleman-Wunsch pairwise global sequence alignment." 
                                             "After you enter the parameters, write your sequence file name.")
parser.add_argument("--match", type=int, required=True, help="Your match score")
parser.add_argument("--mismatch", type=int, required=True, help="Your mismatch score")
parser.add_argument("--gap", type=int, required=True, help="Your gap penalty")
args = parser.parse_args()


###USER VALUES TO CALCULATE SCORES
match = args.match
mismatch = args.mismatch
gap = args.gap


###INPUT FILE SEQUENCE EXTRACTION
input_file = sys.stdin
id_list = []
seq_list = []
for record in SeqIO.parse(input_file, "fasta"):
    #print(record)
    seq_list. append(record.seq)
    id_list.append(record.id)


###SEQUENCES TO BE ALIGNED
seq1 = seq_list[0]
seq2 = seq_list[1]


###MAKE EMPTY MATRIX
def empty_matrix(rows, columns):
    matrix = []
    for x in range(rows):
        matrix.append([])
        for y in range(columns):
            matrix[-1].append(0)
    return matrix


###SCORE FUNCTION
def match_score(base1, base2):
    if base1 == base2:
        return match
    elif base1 == '-' or base2 == '-':
        return gap
    else:
        return mismatch


###NEEDLEMAN WUNSCH ALGORITHM
def needleman_wunsch(seq_1, seq_2):
    n = len(seq_1)
    m = len(seq_2)
    score = empty_matrix(m + 1, n + 1)

    for i in range(0, m + 1):
        score[i][0] = gap * i

    for j in range(0, n + 1):
        score[0][j] = gap * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matching = score[i - 1][j - 1] + match_score(seq_1[j - 1], seq_2[i - 1])
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            score[i][j] = max(matching, delete, insert)
    return score


matrix = needleman_wunsch(seq1, seq2)
print("Similarity value: ", matrix[-1][-1]) #SIMILARITY VALUE OF FORWARD ALGORITHM


###BACKTRACING
def backtracing(seq_1, seq_2):
    score = needleman_wunsch(seq_1, seq_2)
    n = len(seq_1)
    m = len(seq_2)
    align1 = ""
    align2 = ""
    i = m
    j = n
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        if score_current == score_diagonal + match_score(seq_1[j - 1], seq_2[i - 1]):
            align1 += seq_1[j - 1]
            align2 += seq_2[i - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap:
            align1 += seq_1[j - 1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap:
            align1 += '-'
            align2 += seq_2[i - 1]
            i -= 1

    while j > 0:
        align1 += seq_1[j - 1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq_2[i - 1]
        i -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return (align1, align2)

alignment_1, alignment_2 = backtracing(seq1,seq2)


###WRITING THE CLUSTAL FILE
def compare(a, b):
    s = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            s+=str("*")
        else:
            s+=str(" ")
    return s

match = compare(alignment_1, alignment_2)


print("CLUSTAL")

start = 0
end = 60
while len(alignment_1[start:end]) != 0:
    print("\n")
    print(id_list[0] + 12 * " " + alignment_1[start:end])
    print(id_list[1] + 12 * " " + alignment_2[start:end])
    print(23 * " " + match[start:end])
    start = end
    end += 60
