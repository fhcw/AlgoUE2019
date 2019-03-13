import argparse
#import time

parser = argparse.ArgumentParser(description="Inefficient Fibonacci Number Calculation")
parser.add_argument("-n","--number", type=int, required=True, help="Your desired nth Fibonacci number")
parser.add_argument("--all", "--verbosity", action="store_true", dest="allnumbers", help="Prints all Fibonacci numbers up to n")
args = parser.parse_args()

#starttime=time.time()


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    if args.allnumbers:
        liste = []
        for args.number in range(1, args.number + 1):
            #elapsedtime = time.time() - starttime
            liste.append(fibonacci(args.number))
            #print(elapsedtime)
        print(liste)
    else:
        print(fibonacci(args.number))

