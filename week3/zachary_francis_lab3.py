#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from math import sqrt, ceil, floor
from random import random
from scipy.optimize import curve_fit
from time import time

def isPrime(p):
    if p in [0,1]: return True
    lim = ceil(sqrt(p))
    for i in range(2,lim+1):
        if (p % i == 0):
            return False
    return True


def nBitPrime(n):
    f = random()
    r = floor(f * 2 ** n)
    while not isPrime(r):
        f = random()
        r = floor(f * 2 ** n)
    if r in [0, 1, 2]:
        return nBitPrime(n)
    else:
        return r


def factor(pq):
    for i in range(2, pq):
        if (pq % i == 0):
            return (i, pq // i)
    print("NO FACTOR FOUND")
    return (1, pq)


def func_timer(func, *args, **kwargs):
    """Takes a function and its arguments and returns a tuple of the
    results of calling that function plus its execution time"""

    before = time()
    r = func(*args, **kwargs)
    after = time()
    t = (after - before) * 1000
    return (r, t)


def cracking_sim():
    n = 8
    t = 0
    runtimes = {}

    print("Running prime factorization simulation for increasing primes:")
    print("nBits\tTime (ms)")
    # Stop when runtime is greater than 5 minutes
    while t < 1000 * 60 * 5:
        pq = nBitPrime(n) * nBitPrime(n)
        res = func_timer(factor, pq)
        t = res[1]
        runtimes[n] = t
        print(f"{n}\t{t:.1f}")
        n += 1
    return runtimes


def main():
    print("Test generating two 8 bit prime numbers:")
    print(nBitPrime(8))
    print(nBitPrime(8))
    print("")

    print("Test finding two 20 bit prime factors")
    pq = nBitPrime(20) * nBitPrime(20)
    res = func_timer(factor, pq)
    p, q = res[0]
    t = res[1]
    print(f"Found prime factors of {pq} in {t:.2f} ms: {p} and {q}\n")

    # UNCOMMENT TO RUN SIM, TAKES AROUND 10 - 20 MINUTES
    #runtimes = cracking_sim()
    ##Write dict to csv
    #with open('runtimes.csv', 'w') as f:
    #    f.write(f"nBits,ms\n")
    #    for key, val in runtimes.items():
    #        f.write(f"{key},{val}\n")

    runtimes = {}
    with open('runtimes.csv', 'r') as f:
        header = f.readline()
        for line in f:
            n, t = line.strip().split(',')
            runtimes[int(n)] = float(t)

    x = list(runtimes.keys())
    y = list(runtimes.values())

    popt, pcov = curve_fit(lambda x, a, b: a * np.exp(b * x), x, y,
                           p0=[0.0004, 0.6], maxfev=5000)
    a_opt, b_opt = popt
    # curve_fit was not giving well optimized params, so use ones
    # that I got from Excel instead
    a, b = 0.00004, 0.6472
    print(f"SciPy Optimize params: a = {a_opt}, b= {b_opt}")
    print(f"Excel params: a = {a}, b= {b}")

    # Generate curves
    x_fit = np.linspace(8, 40, 100)
    y_fit = a * np.exp(b * x_fit)
    y_opt_fit = a_opt * np.exp(b_opt * x_fit)

    ax = plt.axes()
    ax.scatter(x, y, label='Raw')
    ax.plot(x_fit, y_fit, 'k', label='SciPy')
    ax.plot(x_fit, y_opt_fit, 'r', label='Excel')
    ax.set_title("Time to Calculate Prime Factors")
    ax.set_ylabel("Time (ms)")
    ax.set_xlabel("Size of Factors, in bits")
    ax.legend()
    ax.set_xlim(8, 35)
    ax.set_ylim(0, 2500)
    plt.show()

    print("Calculate the estimated time to crack a 1024 bit key:")
    t = a * np.exp(b * 1024)
    print(f"Milliseconds: {floor(t)}")
    years = t // (1000 * 60 * 60 * 24 * 365)
    print(f"Years: {years}")

    # Copy of output
    #Milliseconds: 26500740389512673587355257439028328171819981224294198865205436769051668720049524742614902606748994846733519995922844428949315763168025520678941154344948365708110820156684349004867573615752925849073415007151070383426335286681978564245460543153621579656939548134239400094390066605981696
    #Years: 8.403329651671953e+272


if __name__ == "__main__":
    main()
