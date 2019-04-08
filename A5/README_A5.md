# Aufgabe A5
## Needleman-Wunsch pairwise global sequence alignment

The task in this assignment is to implement the Needleman-Wunsch (NW) algorithm for global alignment of two sequences. This naturally extends the previous assignments (Manhattan Tourist Problem), i.e. you will need

* a scoring function for computing the similarity of two strings
* a backtracking method to compute the alignment

A simple default scoring function could be

* match: +1
* mismatch : -1
* gap: -2

and you are supposed to give the user the chance to change these numbers via command-line options **--match**, **--mismatch** and **--gap**.

Your tool should read input sequences from a __multi-fasta__ file via STDIN. Such an input file could look like this:

```
>NC_006551.1 |DB.1|386-457|
CCACGGCCCAAGCGAACAGACGGTGATGCGAACTGTTCGTGGAAGGACTAGAGGTTAGAGGAG
ACCCCGTGG
>NC_035889.1 |DB.1|238-307|
CTGGGGCCTGAACTGGAGATCAGCTGTGGATCTCCAGAAGAGGGACTAGTGGTTAGAGGAGAC
CCCCCGG

```

Your tool should write the alignment to STDOUT in __Clustal__ format:

```
CLUSTAL


NC_006551.1            ccacggcccaagcgaacagacggtgatgcgaactgttcgtggaaggactagaggttagag
NC_035889.1            ctggggcctgaactggagatca--gctgtggatctccagaagagggactagtggttagag
                       *   ****  * *       *   * ** * *      *  ** ******* ********


NC_006551.1            gagaccccgtgg
NC_035889.1            gagaccccccgg
                       ********  **
```

Importantly, you are supposed to produce a decoration line for your alignment as shown above, i.e. print (below your alignment) a __*__ for matching positions or a gap character for mismatches or indels. Each block in your alignment should not contain more than 60 aligned positions. If your alignment is longer that 60 positions, introduce line wraps as shown above. In addition, print the computed similarity value (result of the forward algorithm) to STDERR as a single integer number.

Your tool should be named $githubusername-NW.$suffix and an example call should look like this:

* $githubusername-NW.$suffix --match __int__ --mismatch __int__ --gap __int__ [--help] < input.fa

Do not forget to provide a reasonable help message to you users, by adding a **--help** command line option.

Your pull request should include the following:

* your program (source code)

*Submission due date is 28 April 2019, 11:59PM*
