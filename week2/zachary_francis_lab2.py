#!/usr/bin/env python3

from random import shuffle
from time import time

def bubbleSort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

def insertionSort(L):
    for r in range(1,len(L)):
        key = L[r]
        l = r - 1
        while l >= 0 and L[l] > key:
            L[l+1] = L[l]
            l = l - 1
        L[l+1] = key

def merge(A, B):
    L = []
    while A and B:
        if A[0] < B[0]:
            L.append(A.pop(0))
        else:
            L.append(B.pop(0))

    L.extend(A) # No change if list is empty
    L.extend(B) # No change if list is empty
    return L

def mergeSort(L):
    if len(L) < 2:
        return L[:]

    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)


def sort_demos():
    print("Verifying sort fuctions works with list 1 - 10...\n")
    A = [i for i in range(1,11)]
    shuffle(A)
    print("Random List:")
    print(A,"\n")

    print("Bubble Sort:")
    bubbleSort(A)
    print(A, "\n")

    shuffle(A)
    print("Insertion Sort:")
    insertionSort(A)
    print(A, "\n")

    shuffle(A)
    print("Merge Sort:")
    print(mergeSort(A), "\n")


def sort_timer(func, L):
    before = time()
    func(L)
    after = time()
    return (after - before) * 1000


def time_table(low, high, step):
    L = [i for i in range(high)]
    shuffle(L)

    print(f"N\tBubble\tInsert\tMerge")
    for i in range(low, high + step, step):
        bubble = sort_timer(bubbleSort, L[:i])
        insertion = sort_timer(insertionSort, L[:i])
        merge = sort_timer(mergeSort, L[:i])
        print(f"{i}\t{bubble:.1f}\t{insertion:.1f}\t{merge:.1f}")

def main():
    sort_demos()
    time_table(100, 5000, 100)


if __name__ == "__main__":
    main()
