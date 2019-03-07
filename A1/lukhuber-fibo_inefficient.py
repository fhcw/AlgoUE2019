#!/usr/bin/python3

from argparse import ArgumentParser

def Main():
    parser = ArgumentParser(prog="Fibonacci Sequence Calculator")

    parser.add_argument("-n", type = int, nargs = 1, help = "Number of steps in the fibonacci sequence")
    parser.add_argument("--all", default = False, action = "store_true", help = "Displays each step in the fibonacci sequence until n")

    arguments = parser.parse_args()

    numberOfSteps = arguments.n[0]
    displayAllValues = arguments.all
    listResults = []

    for i in range (0, numberOfSteps + 1):
        listResults.append(i)

    Fibonacci_Generator(numberOfSteps, listResults)
    Display_Result(listResults, displayAllValues)



def Fibonacci_Generator(numberOfSteps, arr=[]):
    if numberOfSteps == 0:
        return 0 
    elif numberOfSteps == 1:
        return 1
    else:
        result = Fibonacci_Generator(numberOfSteps - 1, arr) + Fibonacci_Generator(numberOfSteps - 2, arr)
        arr[numberOfSteps] = result
        return result



def Display_Result(result, displayAllValues):
    if displayAllValues == False:
        print(result[-1])
    else:
        for value in result:
            print(value, end=' ')
        print()



if __name__ == "__main__":
    Main()