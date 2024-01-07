#!/usr/bin/env python3

import re

def printMatrix(m):
    for row in m:
        print(row)

def parenStr(tm, i, j):
    if i == j:
        return 'A' + str(i)
    else:
        split = tm[i][j]
        left = parenStr(tm, i, split)
        right = parenStr(tm, split+1, j)
        return '(' + left + ')(' + right + ')'

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    trace = [[None for i in range(n)] for j in range(n)]

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1

            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    trace[i][j] = k

    printMatrix(m)
    s = parenStr(trace, 0, n-1)
    print()
    print(s)
    print("\nRemove the single matrix parens for easier reading:")
    print(re.sub(r'(\d)A', r'\1*A', re.sub(r'\((A\d+)\)', r'\1', s)), "\n")
    return m[0][n-1]

dims = [30,35,15,5,10,20,25]
print(chainMatrix(dims))
