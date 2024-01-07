#!/usr/bin/env python3

import csv

def loadInvestments(fileName):
    with open('Metro.csv','r') as f:
        reader = csv.DictReader(f)
        investments = []
        for row in reader:
            name = row['RegionName']
            cost = int(row['2020-01'])
            gain = cost - int(row['2019-01'])
            investments.append((name, cost, gain))
    return investments


def optimizeInvestments(investments, budget, inc=1):
    # Round the increment if something other than 1
    if inc == 1:
        costs = [0] + [x[1] for x in investments]
    else:
        costs = [0] + [(x[1]//inc+1)*inc for x in investments]
    gains = [0] + [x[2] for x in investments]
    fund = range(0, budget+inc, inc)

    # The first row and column will be zeroes
    best_invest = [[0 for _ in fund] for _ in costs]
    for i in range(1, len(costs)):
        for j in range(1, len(fund)):
            if costs[i] > fund[j]:
                best_invest[i][j] = best_invest[i-1][j]
            else:
                best_invest[i][j] = max(
                    best_invest[i-1][j],
                    best_invest[i-1][j-(costs[i]//inc)]+gains[i]
                )
    # Perform the traceback to get the investments
    invest_list = []
    j = len(fund) - 1
    for i in range(len(costs)-1, 0, -1):
        if best_invest[i][j] == 0:
            break
        if best_invest[i][j] != best_invest[i-1][j]:
            invest_list.append(investments[i-1])
            j = j - (costs[i] // inc)

    return best_invest[-1][-1], invest_list


def main():
    budget = 1000000 # Total budget to spend
    increment = 1000 # What cost to increment by

    test_set = [
        ('A', 4, 5),
        ('B', 3, 4),
        ('C', 2, 3),
        ('D', 1, 2)
    ]
    max_val, picks = optimizeInvestments(test_set, 6)
    print(f"Max val: {max_val}, by picking:")
    for x in picks:
        print(f"\t{x[0]}, Weight: {x[1]}, Val: {x[2]}")
    print()

    investments = loadInvestments('Metro.csv')
    max_gain, best_invests = optimizeInvestments(investments, budget, increment)

    print(f"The maximum gain for a budget of ${budget} is ${max_gain}.")
    print("Purchase homes in the following cities for maximum profit:")
    for x in best_invests:
        print(f"\t{x[0]} for ${x[1]} with a return of ${x[2]}")

    total_cost = sum([x[1] for x in best_invests])
    print(f"Total cost is ${total_cost}")


if __name__ == '__main__':
    main()
