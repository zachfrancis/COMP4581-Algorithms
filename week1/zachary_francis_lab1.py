#!/usr/bin/env python3

def printMatrix(m):
    for row in m:
        print(row)

def getDimensions(m):
    return (len(m), len(m[0]))

def matrixMult(A, B):
    dimA, dimB  = getDimensions(A), getDimensions(B)
    if not (dimA[1] == dimB[0]):
        print("Cannot multiply a {}x{} matrix by {}x{} matrix".format(dimA[0],dimA[1],dimB[0],dimB[1]))
        return None

    print("Multiplying a {}x{} matrix by {}x{} matrix:".format(dimA[0],dimA[1],dimB[0],dimB[1]))

    C = [[0 for i in range(0, dimB[1])] for j in range(0, dimA[0])]
    for i in range(0, dimA[0]):
        for j in range(0, dimB[1]):
            sum = 0
            for k in range(0, dimA[1]):
                sum = sum + A[i][k] * B[k][j]
            C[i][j] = sum

    return C


# Testing code
# Test1
A = [[ 2, -3, 3],
    [-2, 6, 5],
    [ 4, 7, 8]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7]]

C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test2
A = [[ 2, -3, 3, 0],
    [-2, 6, 5, 1],
    [ 4, 7, 8, 2]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7]]

C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test3
A = [[ 2, -3, 3, 5],
    [-2, 6, 5, -2]]
B = [[-1, 9, 1],
    [ 0, 6, 5],
    [ 3, 4, 7],
    [ 1, 2, 3]]

C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
