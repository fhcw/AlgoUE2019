// # Aufgabe A2 
// ## Towers of Hanoi

// The task is to solve the n-disc Towers of Hanoi puzzle.

// Implement a program that accepts an integer via command line option __-n__
// and prints instructions to STDOUT as follows:

// Move disk from X to Y

// Likewise, the tool should print the total number of disc move operations
// to STDERR upon finishing the computation. Allow the user to obtain some information on your tool via a __--help__ option. The program should be named as
// *` $githubusername-TowersOfHanoi.$suffix -n [--help]`

// Measure the runtime of your tool, ensuring that STDOUT is redirected to a
// file rather than displayed via the console (which would unnecessarily blow
// up runtime). You might employ the concept of subshells to get this done.

// Plot the runtime of your program (in seconds) vs size of the Hanoi puzzle and create a PDF graph. Your pull request should include the following files:

// * your program
// * A file containing STDOUT of your program up to at least n=25. The name of this file should be `$githubusername-TowersOfHanoi.out`
// * a PDF plot of runtime vs n named `$githubusername-TowersOfHanoi_runtime.pdf`


#include <iostream>
#include <string.h>
using namespace std;

void hanoiTowers (int, char, char, char);
int countHanoiMoves (int, char, char, char);

int main(int argc, char** argv)
{             
    if (argc == 2 && strcmp(argv[1], "--help")==0) {
        cout << "Enter the flag -n after the executable file and provide a number [n] to define the number of discs." << endl;
        }

    if (argc == 3 && strcmp(argv[1], "-n") == 0) {
        int discNumber = atoi(argv[2]);
        hanoiTowers(discNumber, 'A', 'C', 'B');
        cerr << countHanoiMoves(discNumber, 'A', 'C', 'B') << endl;
        return 0;
    }
}


void hanoiTowers (int num, char frompeg, char topeg, char auxpeg)
{
    if (num == 1) {
        cout << "Move disk 1 from peg " << frompeg << " to peg " << topeg << endl;
        return;
    }

    hanoiTowers(num - 1, frompeg, auxpeg, topeg);
    cout << "Move disk " << num << " from peg " << frompeg << " to peg " << topeg << endl;
    hanoiTowers (num - 1, auxpeg, topeg, frompeg);
}


int countHanoiMoves (int num, char frompeg, char topeg, char auxpeg)
{
   int count = 0;
   if (num > 0){
       count = countHanoiMoves (num-1, frompeg, auxpeg, topeg);
       count++;
       count += countHanoiMoves(num-1, auxpeg, topeg, frompeg);
   }
   return count;
}