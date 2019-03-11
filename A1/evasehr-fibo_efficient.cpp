// Fibonacci Numbers - efficient algorithm
// by Eva M. Sehr
// 2019-03-11

// The task is to compute the the first n Fibonacci fiboNumbers. 
// Implement an ineffieient as well as an efficient version as two standalone programs that should accept 
// an integer via command line option -n and print the nth Fibonaci number to STDOUT. 
// Implement an optional command line switch --all that prints all Fibonacci fiboNumbers up to n as a comma-separated list to STDOUT.
// Calculate the runtime.

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iterator>
#include <vector>
using namespace std;


int main(int argc, char** argv)
{             
    if (argc == 2 && strcmp(argv[1], "--help")==0) {
        cout << "Enter a number n after the executable file, that will print you the n-th Fibonacci number, \nor provide the additional option --all to print all Fibonacci fiboNumbers until the nth number." << endl;
        }

    else if (argc == 3 && strcmp(argv[2], "--all")==0) {
        int inNumber = atoi(argv[1]);      
        int fiboNumbers[inNumber] = {0, 1};
        for (int i = 2; i <= inNumber; i++) {
            fiboNumbers[i] = fiboNumbers[i - 1] + fiboNumbers[i - 2];
        }
        for (int i = 1; i <= inNumber; i++) {
            cout << fiboNumbers[i] << ", ";
        }
        cout << endl;
    }
        
    else {
        int inNumber = atoi(argv[1]);
        int fiboNumbers[inNumber] = {0, 1};
        for (int i = 2; i <= inNumber; i++) {
            fiboNumbers[i] = fiboNumbers[i - 1] + fiboNumbers[i - 2];
        }
        cout << fiboNumbers[inNumber] << " " << endl;
    }

return 0;
}