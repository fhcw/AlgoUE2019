

import argparse

parser=argparse.ArgumentParser(description="Efficient mehtod: memoritation tool has been implemented to improve the runtime")
parser.add_argument('-n','--fibonacci_integer', type = int, required=True, help = "the n-th number for the fibonacci function")
group = parser.add_mutually_exclusive_group()
group.add_argument('-all', '--allnumbers', action='store_true',help="returns a comma separated list of all fibo-numbers")
args = parser.parse_args()
n = args.fibonacci_integer


def fibonacci_function(n):
    if n in fmemory:
        return fmemory[n]
    if n <= 2:
        return 1
    else:
        f = (fibonacci_function(n-1))+(fibonacci_function(n-2))
        fmemory[n] = f 
        return f

def printAll(i):
    j = 1
    while j <= n:
        outputLine.append(fibonacci_function(j))
        j += 1
    return outputLine

outputLine = list()
fmemory = {}

if args.allnumbers:
  print(printAll(n))

else:
   print(fibonacci_function(n))

