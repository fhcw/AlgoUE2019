// Fibonacci numbers
// by Eva M. Sehr
// 2019-03-01

// The task is to compute the the first n Fibonacci numbers. 
// Implement an ineffieient as well as an efficient version as two standalone programs that should accept 
// an integer via command line option -n and print the nth Fibonaci number to STDOUT. 
// Implement an optional command line switch --all that prints all Fibonacci numbers up to n as a comma-separated list to STDOUT.
// Zeit messen wie lange es dauert

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

int fib(int x);

int main(int argc, char** argv)
{             
    if (argc == 2 && strcmp(argv[1], "--help")==0) {
        cout << "Enter a number (n) after the executable file, that will print you the n-th Fibonacci number, \nor provide the additional flag --all after the number to print all Fibonacci numbers until the given nth number." << endl;
    }
    else if (argc == 3 && strcmp(argv[2], "--all")==0) {
        int inNumber = atoi(argv[1]);        
        int i=1;
        while(i <= inNumber) {
            cout << fib(i) << ", ";
            i++;
        } 
        cout << endl;
    }   
    else {    
    int inNumber = atoi(argv[1]);
    cout << fib(inNumber) << endl;
    }   
return 0;
}


// Rekursive Fibonacci Funktion
int fib(int x) {
    if((x==1)||(x==0)) {
      return(x);
    }
    else {
        return(fib(x-1)+fib(x-2));
    }
}