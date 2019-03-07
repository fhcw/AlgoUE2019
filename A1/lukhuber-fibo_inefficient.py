#!/usr/bin/python3

from argparse import ArgumentParser
from datetime import datetime

def Main():
    parser = ArgumentParser(prog="Fibonacci Sequence Calculator")

    parser.add_argument("-n", type = int, nargs = 1, help = "Number of steps in the fibonacci sequence")
    parser.add_argument("--all", default = False, action = "store_true", help = "Displays each step in the fibonacci sequence until n")

    arguments = parser.parse_args()

    numberOfSteps = arguments.n[0] + 1
    displayAllValues = arguments.all

    startTime = datetime.now()
    result = Fibonacci_Generator(numberOfSteps)
    Display_Result(result, displayAllValues)
    endTime = datetime.now()

    print("Runtime: ", endTime.microsecond - startTime.microsecond)

def Fibonacci_Generator(numberOfSteps):
    result_list = [1, 1]    

    for i in range(2, numberOfSteps):
        result_list.append(result_list[i-2] + result_list[i-1])

    return result_list



def Display_Result(result, displayAllValues):
    if displayAllValues == False:
        print(result[-1])
    else:
        for value in result:
            print(value)



if __name__ == "__main__":
    Main()