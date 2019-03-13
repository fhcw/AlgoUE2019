import argparse
#import time

parser = argparse.ArgumentParser(description="Efficient Fibonacci Number Calculation")
parser.add_argument("-n","--number", type=int, required=True, help="Your desired nth Fibonacci number")
parser.add_argument("--all", "--verbosity", action="store_true", dest="allnumbers", help="Prints all Fibonacci numbers up to n")
args = parser.parse_args()

#starttime=time.time()
fibo_storage = {}


def fibonacci(n):
    if n in fibo_storage:
        return fibo_storage[n]

    if n == 1:
        fibo = 1
    elif n == 2:
        fibo = 1
    elif n > 2:
        fibo = fibonacci(n-1) + fibonacci(n-2)

    fibo_storage[n] = fibo
    return fibo


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



