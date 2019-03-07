#!/usr/bin/python3

## TODO: --all funktioniert noch nicht, weil keine Liste von Fibonacci_Generator() zurückgegeben wird,
## sondern nur ein int.

from argparse import ArgumentParser
import cProfile

def Main():
    parser = ArgumentParser(prog="Fibonacci Sequence Calculator")

    parser.add_argument("-n", type = int, nargs = 1, help = "Number of steps in the fibonacci sequence")
    parser.add_argument("--all", default = False, action = "store_true", help = "Displays each step in the fibonacci sequence until n")

    arguments = parser.parse_args()

    numberOfSteps = arguments.n[0] + 1
    displayAllValues = arguments.all

    result = Fibonacci_Generator(numberOfSteps)

    Display_Result(result, displayAllValues)


def Fibonacci_Generator(numberOfSteps):
    if numberOfSteps == 0:
        return 0
    elif numberOfSteps == 1:
        return 1
    else:
        return Fibonacci_Generator(numberOfSteps - 1) + Fibonacci_Generator(numberOfSteps - 2)



def Display_Result(result, displayAllValues):
    if displayAllValues == False:
        print(result)
    else:
        for value in result:
            print(value)



if __name__ == "__main__":
    Main()