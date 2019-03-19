#!/usr/bin/python3

"""The task is to solve the n-disc Towers of Hanoi puzzle.
Implement a program that accepts an integer via command line option
-n and prints instructions to STDOUT as follows:
Move disk from X to Y
Likewise, the tool should print the total number of disc move operations
to STDERR upon finishing the computation.
Allow the user to obtain some information on your tool via a --help option.
"""

import argparse
import sys

parser = argparse.ArgumentParser(description="Output of steps to move Tower of Hanoi.")
parser.add_argument('-n','--n_disks', required=True, type=int, metavar=' ', help='enter the number of n_disks')
args = parser.parse_args()
n_disks = args.n_disks

"""The task of this funktion is to solve the known problem of "Tower of Hanoi" 
in this program were 3 Sticks where all the sticks n are located on disc A and these should
be moved to disc C, with every step, only one disc is allowed to move"""



count = 0
def hanoi(n_disks, disc_A, disc_B, disc_C):
    global count
    if n_disks == 1:
        print('Move disk 1 from stick {} to stick {}.'.format(disc_A, disc_C))
        count += 1
        return count


    hanoi(n_disks - 1, disc_A, disc_C, disc_B)
    print('Move disk {} from stick {} to stick {}.'.format(n_disks, disc_A, disc_C))
    hanoi(n_disks - 1, disc_B, disc_A, disc_C)


#n_disks = int(input('Enter number of n_disks: '))
n_disks = args.n_disks
hanoi(n_disks, 'A', 'B', 'C')
print("Total number of moves for ",n_disks, " disc(s) is", 2^n_disks - 1,".\n")
