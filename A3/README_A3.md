# Aufgabe A3
## Manhattan Tourist Problem - Part 1

The task is to solve the Manhattan Tourist Problem for given, arbitrary grid weights. Compute the longest path from source (0,0) to sink (N,N) via dynamic programming. In a first step we restrict the grid to horizontal and vertical edges, respectively.

For an N\*N grid we have (N-1)\*N horizontal edges and N\*(N-1) vertical edges, respectively. An example input file for a 5*5 grid with horizontal and vertical edges looks like this:

```
G_down: 4 5
  0.12   0.79   0.50   0.56   0.39
  0.93   0.14   0.82   0.80   0.13
  0.71   0.37   0.49   0.94   0.88
  0.59   0.52   0.40   0.87   0.16
---
G_right: 5 4
  0.43   0.21   0.55   0.61
  0.61   0.89   0.52   0.54
  0.44   0.85   0.74   0.12
  0.56   0.91   0.61   0.24
  0.56   0.42   0.27   0.49
---
```

The file consists of two matrices for vertical (G_down) and horizontal (G_right) edges. Each matrix block contains tab-separated floating point values and is closed by three dashes. Beware that the numbers next to the identifiers G_down and G_right might be misleading, i.e., **do not** parse the matrix dimensions from these numbers but compute them on the fly when parsing the matrices.

Ensure to check for consistency of the input files. In particular check if you read the correct number of items in every line (implicitly assuming that the dimensions obtained from parsing the first lines of each matrix is correct). A simple check if your tool parses the input as required is to remove the two integers next to G_down and G_right.

Within the *random_matrices* folder you will find a set of randomly generated input files that follow the above specification. For the first part of this exercise choose an input file from the *rmHV_10_X* (dimension 10\*10, horizontal,vertical) set as well as one file from the *rmHV_999_X* (dimension 999\*999). Ensure with you colleagues that no two persons select the same input files.

---

Implement a program that a) reads from STDIN a file as specified above and b) computes the weight of the longest path from source to sink. The program should print the computed floating point number to STDOUT. (Recall that this procedure essentially corresponds to the forward recursion of the Needleman-Wunsch algorithm for pairwise global sequence alignment.)

Your program should be named *$githubusername-ManhattanTouristHV.$suffix* and an example call should look like this:

*$githubusername-ManhattanTouristHV.$suffix < rmHV_10_5*

Keep in mind **not to** provide the dimension of the input matrices to your program at runtime. Your implementation should be able to process input data as specified above in any dimension.

Your pull request should include the following:

* your program (source code)
* wheight of the longest path for your input files (one for dim 10, and one for dim 999, respectively)
* let me know which input file you selected (via writing the file name in you ping message, e.g. `@mtw please review rmHV_10_5`)

**Submission due date is 3 April 2019 10:00 CEST**
