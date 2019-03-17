#!/usr/bin/env python3

#AlgoUE BIOINF20
#A1 - Towers Of Hanoi
#Dominic Viehböck

import sys
from argparse import ArgumentParser

def Main():
    # ArgumentParser
    parser = ArgumentParser(description="Calculate number of moves for Towers of Hanoi Problem given a number of discs."
                                        "STDOUT = Movements, STDERR = Nr. of Steps")
    parser.add_argument("-n", type=int, default = 10, help="Number of discs")

    args = parser.parse_args()

    def Hanoi(n, first, helper, target):
        """Move disc from tower 'first' [left argument] to tower 'target' [right argument] over intermediate tower
        'helper."""
        if n > 0:
            Hanoi.movecount += 1
            # move tower of size n - 1 to helper:
            Hanoi(n - 1, first, target, helper)
            print("Move disc from ", first, " to ", target)
            # move tower of size n-1 from helper to target
            Hanoi(n - 1, helper, first, target)

    n = args.n
    Hanoi.movecount = 0
    Hanoi(n, "X", "Y", "Z")
    print(Hanoi.movecount, file=sys.stderr)

if __name__ == "__main__":
    Main()

