#!/usr/bin/python3

from argparse import ArgumentParser
import sys

def Main():
    parser = ArgumentParser(prog = "Towers of Hanoi", description = "Calculates the steps necessary to move n disks from one stack to another stack using the limitations of the towers-of-hanoi algorithm. The number of necessary steps is piped to STDERR.")

    parser.add_argument("-n", type = int, nargs = 1, help = "Height of the stack")

    arguments = parser.parse_args()

    numberOfDisks = arguments.n[0]
    moveDisk.steps = 0  

    moveStack(numberOfDisks, "1. Stack", "2. Stack", "3. Stack")

    print("Number of necessary moves: ", moveDisk.steps, file=sys.stderr)



def moveStack(numberOfDisks, fromStack, toStack, usingStack):
    if numberOfDisks >= 1:
        moveStack(numberOfDisks - 1, fromStack, usingStack, toStack)
        moveDisk(fromStack,toStack)
        moveStack(numberOfDisks - 1, usingStack, toStack, usingStack)



def moveDisk(fromStack, toStack):
    moveDisk.steps += 1
    print("Moving disk from", fromStack, "to", toStack)



if __name__ == "__main__":
    Main()