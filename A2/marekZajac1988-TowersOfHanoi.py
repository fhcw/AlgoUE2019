#!/usr/bin/python3.6

import sys
import argparse
parser = argparse.ArgumentParser(description="Calculate a Towers of Hanoi moveset for a certain amount of disks. Number of turns is printed to STDERR")
parser.add_argument("input", type=int,
                    help="input integer to calculate moves for n disks")
parser.add_argument("-n", action="store_true",
                   help="output only nth number of fibonacci sequence")
args = parser.parse_args()
input = args.input

def HanoiTowers(n, fromPeg, toPeg):
    if n == 1:
        print("Move disk from " + str(fromPeg) + " to " + str(toPeg) + ".")
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n - 1, fromPeg, unusedPeg)
    print("Move disk from " + str(fromPeg) + " to " + str(toPeg))
    HanoiTowers(n - 1, unusedPeg, toPeg)
    return

if args.n:
    HanoiTowers(input, 1, 3)
    sys.stderr.write(str(2**input-1))