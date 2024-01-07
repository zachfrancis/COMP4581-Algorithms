#!/usr/bin/env python3 

# Below are two algorithms (DAC and DP) to compute the
# minimum number of coins required to produce A cents worth of change
# The DP version also prints out the coins needed to produce this min
from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
    for currentCoin in coins: # Check all coins
        # If we can give change
        if (amount - currentCoin) >= 0:
            # Calculate the optimal for currentCoin
            currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
            minCoins = min(minCoins, currentMin)
    return minCoins


# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the initial tables
    minCoins = [float('inf') for _ in range(amount+1)]
    traceback = [float('inf') for _ in range(amount+1)]

    # Fill in the base case(s)
    minCoins[0] = 0
    traceback[0] = 0

    # Fill in the rest of the table
    for val in range(amount+1):
        for coin in coins:
            if val - coin >= 0:
                currentMin = minCoins[val - coin] + 1
                if currentMin < minCoins[val]:
                    minCoins[val] = currentMin
                    traceback[val] = coin

    # Perform the traceback to print result
    while amount > 0:
        print(traceback[amount])
        amount = amount - traceback[amount]

    return minCoins[-1] # return optimal number of coins

C = [1,5,10,12,25] # coin denominations (must include a penny)

A = int(input('Enter desired amount of change: '))
assert A>=0

print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")

print()
print("DP:")
t1 = time()
numCoins = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
