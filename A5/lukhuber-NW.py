#!/usr/bin/python3

import argparse
import sys

def Main():

    ## Initialize arguments
    args = initArguments()

    ## Save given parameters from arguments globally
    global mismatch    
    mismatch = args.mismatch
    global gap
    gap = args.gap
    global match
    match = args.match

    ## Initialize the two sequences
    seq1 = sequence("first")
    seq2 = sequence("second")

    ## Sort longer sequence into seq1 and shorter in seq2
    long_seq = seq1.sequence if seq1.sequence_len >= seq2.sequence_len else seq2.sequence
    short_seq = seq2.sequence if seq1.sequence_len >= seq2.sequence_len else seq1.sequence

    seq1.sequence = long_seq
    seq2.sequence = short_seq

    ## Initialize the matrix
    mat = matrix(seq1, seq2)

    ## Adapt sequences and clustal according to matrix
    seq1.sequence = seq1.adaptSequence(mat.steps, "long")
    seq2.sequence = seq2.adaptSequence(mat.steps, "short")

    clustal = compareSequences(seq1, seq2, mat)
    
    ## Print Results
    printResult(seq1, seq2, clustal, mat)

    #print(mat.steps)

    ## Print matrix
    #for i, v in enumerate(mat.matrix):
    #    print(mat.matrix[i])



class sequence():

    def __init__(self, order):

        self.sequence = self.parseSequenceFromInput(order)
        self.header = self.parseHeaderFromInput(order)
        self.sequence_len = len(self.sequence)
        

    def parseSequenceFromInput(self, order):
        
        ## Initialize string and bool flag
        found = False
        sequence = ""

        if order == "first":

            ## Saving sequence in variable
            for line in sys.stdin:

                ## Break for-loop, when second sequence is found
                if line[0] == '>' and found == True:
                    break

                ## Setting flag after first '>' is found
                if line[0] == '>':
                    found = True
                    continue

                ## Saving sequence in variable
                sequence += line.replace('\n', '')
            
            ## Reset STDIN for further parsing
            sys.stdin.seek(0) 

            return sequence
        
        elif order == "second":
			
			## Saving sequence in variable
            for line in sys.stdin:

                ## Skip Header from first sequence and set flag (lock)
                if line[0] == '>' and found == False:
                    found = True
                    continue

                ## Skip Header from second sequence and set flag (unlock)
                if line[0] == '>' and found == True:
                    sequence = ''
                    continue

				## Saving sequence in variable
                if found == True:
                    sequence += line.replace('\n', '')
                
            ## Reset STDIN for further parsing
            sys.stdin.seek(0)
            
            return sequence
        
    
    def parseHeaderFromInput(self, order):
        
		## Initialize string and bool flag
        found = False
        header = ""
		
        if order == "first":
			
			## Saving header in variable
            for line in sys.stdin:
                if line[0] == '>' and found == False:
                    pos = line.find('|')
                    header = line[1:pos - 1]
                    found = True
                    break
				
				
			## Reset STDIN for further parsing
            sys.stdin.seek(0)
            
            return header
			
        elif order == "second":
			
            for line in sys.stdin:
				
                ## Find first header, set flag and skip line
                if line[0] == '>' and found == False:
                    found = True
                    continue
				
                ## Find second header using flag and save header in variable
                if line[0] == '>' and found == True:
                    pos = line.find('|')
                    header = line[1:pos - 1]
                    break
					
			## Reset STDIN for further parsing
            sys.stdin.seek(0)
            
            return header


    def adaptSequence(self, steps, length):
        ## Transform sequence from string into char array
        chars = []

        for char in self.sequence:
            chars.append(char)

        ## Reverse steplist as we want to alter the sequence from back to front
        steps = steps[::-1]

        if length == "long":
            for i, v in enumerate(steps):
                i = (i * -1)
                if v == 2:
                    if i == 0:
                        chars.append('-')
                        continue
                    chars.insert(i, "-")

        elif length == "short":
            for i, v in enumerate(steps):
                i = (i * -1)
                if v == 1:
                    if i == 0:
                        chars.append('-')
                        continue
                    chars.insert(i, "-")

        
        ## Transform chars back into string
        sequence = ""

        for char in chars:
            sequence += char
        
        return sequence



class matrix():
	
    def __init__(self, seq_l, seq_s):

        self.matrix = self.createMatrix(seq_l, seq_s)
        self.matrix = self.prepareMatrix(self.matrix)
        self.matrix = self.fillMatrix(seq_l, seq_s, self.matrix)
        self.steps = self.getSteps()
        self.score = 0

        ## Pop first item from steps, as this will always be diagonal
        self.steps.pop(0)


    def createMatrix(self, seq_l, seq_s):

        ## Initialize columns and rows.
        cols = seq_s.sequence_len
        rows = seq_l.sequence_len

        ## Initialize matrix
        matrix = [[0 for x in range(cols+1)] for y in range(rows+1)]

        return matrix

        
    def prepareMatrix(self, matrix):

        ## Prepare first item of each row
        for i, v in enumerate(matrix):
            matrix[i][0] = i * -1
        
        ## Prepare all items in first row
        for i, v in enumerate(matrix[0]):
            matrix[0][i] = i * -1

        return matrix
	

    def fillMatrix(self, seq_l, seq_s, matrix):

        ## Initialize columns and rows.
        cols = seq_s.sequence_len
        rows = seq_l.sequence_len

        ## Needleman Wunsch logic for filling matrix
        for r in range(0, rows):
            for c in range(0, cols):
                if seq_l.sequence[r] == seq_s.sequence[c]:
                    rgh = matrix[r+1][c] + gap
                    dwn = matrix[r][c+1] + gap
                    dig = matrix[r][c] + match
                else:
                    rgh = matrix[r+1][c] + gap
                    dwn = matrix[r][c+1] + gap
                    dig = matrix[r][c] + mismatch

                matrix[r+1][c+1] = max(rgh, dwn, dig)
        
        return matrix
	
	
    def getSteps(self):
        
        ## Initialize variables for position in matrix
        col_pos = -1
        row_pos = -1

        steps = []

        ## Initialize variables for loop and break condition
        col_max = len(self.matrix[0]) * -1
        row_max = len(self.matrix) * -1

        ## Logic for step calculation
        while col_pos > col_max and row_pos > row_max:
            hrz = self.matrix[row_pos][col_pos] + self.matrix[row_pos][col_pos-1]
            ver = self.matrix[row_pos][col_pos] + self.matrix[row_pos-1][col_pos]
            dia = self.matrix[row_pos][col_pos] + self.matrix[row_pos-1][col_pos-1]

            ## Get variable with highest value
            values = (dia, ver, hrz)
            highest = values.index(max(values))

            ## Add diagonal item to score and move pos
            if highest == 0:
                steps.insert(0, 0)
                col_pos += -1
                row_pos += -1
            
            ## Add horizontal item to score and move pos
            elif highest == 2:
                steps.insert(0, 2)
                col_pos += -1

            ## Add vertical item to score and move pos
            elif highest == 1:
                steps.insert(0, 1)
                row_pos += -1

        return steps
		


def initArguments():
    parser = argparse.ArgumentParser(prog='lukhuber-NW.py', description='Aligns two different DNA sequences \
        Requires an input in form of a multi-fasta file via STDIN. The program writes the final score to STDERR, \
        if STDERR is piped into a file at program call.')

    parser.add_argument('--match', dest = 'match', default = 1, type = int, help = 'Scoring value for a match. Default = +1')
    parser.add_argument('--mismatch', dest = 'mismatch', default = -1, type = int, help = 'Scoring value for a mismatch. Default = -1')
    parser.add_argument('--gap', dest = 'gap', default = -2, type = int, help = 'Scoring value for a gap. Default = -2')

    return parser.parse_args()



def compareSequences(seq1, seq2, matrix):
    clustal = ''
    score = 0

    for i, v in enumerate(seq2.sequence):

        ## Add ' ' in case of gap. Score + gap
        if seq2.sequence[i] == '-' or seq1.sequence[i] == '-':
            clustal += ' '
            score += gap

        ## Add '*' in case of match. Score + match
        elif seq2.sequence[i] == seq1.sequence[i]:
            clustal += '*'
            score += match

        ## Add ' ' in case of mismatch. Score + mismatch
        elif seq1.sequence[i] != seq2.sequence[i]:
            clustal += ' '
            score += mismatch

        matrix.score = score


    return clustal



def printResult(seq1, seq2, clustal, matrix):

    ## Calculate how many lines will be needed
    lines = round(len(seq1.sequence) / 60 + 0.5)
    
    ## Print both sequences in steps of 60
    for i in range (1, lines + 1):
        if i == 1: 
            print(seq1.header, '  ', seq1.sequence[0:60])
            print(seq2.header, '  ', seq2.sequence[0:60])
            print('              ', clustal[0:60])
            print("")
        else:
            print(seq1.header, '  ', seq1.sequence[i*60-60:i*60])
            print(seq2.header, '  ', seq2.sequence[i*60-60:i*60])
            print('              ', clustal[i*60-60:i*60])
            print("")

    print("Score: ", matrix.score, file = sys.stderr)



if __name__ == "__main__":
    Main()