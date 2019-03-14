# Aufgabe A2
## Towers of Hanoi

The task is to solve the n-disc Towers of Hanoi puzzle.

Implement a program that accepts an integer via command line option __-n__
and prints instructions to STDOUT as follows:

Move disk from X to Y

Likewise, the tool should print the total number of disc move operations
to STDERR upon finishing the computation. Allow the user to obtain some information on your tool via a __--help__ option. The program should be named as

*` $githubusername-TowersOfHanoi.$suffix -n [--help]`

Measure the runtime of your tool, ensuring that STDOUT is redirected to a
file rather than displayed via the console (which would unnecessarily blow
up runtime). You might employ the concept of subshells to get this done.

Plot the runtime of your program (in seconds) vs size of the Hanoi puzzle and create a PDF graph. Your pull request should include the following files:

* your program
* A file containing STDOUT of your program up to at least n=25. The name of this file should be `$githubusername-TowersOfHanoi.out`
* a PDF plot of runtime vs n named `$githubusername-TowersOfHanoi_runtime.pdf`
