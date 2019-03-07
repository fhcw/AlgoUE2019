# Aufgabe A1
## Fibonacci numbers

The task is to compute the the first *n* Fibonacci numbers. Implement
an ineffieient as well as an efficient version as two standalone
programs that should accept an integer via command line option __-n__
and print the nth Fibonaci number to STDOUT. Implement an optional
command line switch __--all__ that prints all Fibonacci numbers up to
n as a comma-separated list to STDOUT. Document your tools
accordinglt, i.e. provide at least a __--help__ switch that prints
simple usage instructions to STDOUT. The file must be named according
to the following schema:

* $githubusername-fibo_inefficient.$suffix -n <int> [--all] [--help]
* $githubusername-fibo_efficient.$suffix -n <int> [--all] [--help]

Measure the runtime of both tools for different parameters of n,
e.g. via the `time` command. Plot the runtime of both approaches as a
function of n in a single PDF graph. The filename should be
`$githubusername-fibo_runtime.pdf`.
