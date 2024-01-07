#!/usr/bin/env python3

from collections import defaultdict
import pandas as pd

def max_profit_DAC(ser, low=0, high=None):
    if high is None: high = len(ser)-1

    # Base case
    if low == high:
        if ser[low] > 0:
            return (low, high, ser[low])
        else:
            return (low, high, 0)

    # Divide
    mid = (low + high) // 2

    # Conquer
    maxLeft = max_profit_DAC(ser, low, mid)
    maxRight = max_profit_DAC(ser, mid+1, high)

    # Find max between left and center
    maxLeftToCenter = leftToCenter = 0
    max_i_left = mid
    for i in range(mid, low-1, -1):
        leftToCenter += ser[i]
        max_i_left = i if leftToCenter > maxLeftToCenter else max_i_left
        maxLeftToCenter = max(leftToCenter, maxLeftToCenter)

    # Find max between right and center
    maxRightToCenter = rightToCenter = 0
    max_i_right = mid+1
    for i in range(mid+1, high+1):
        rightToCenter += ser[i]
        max_i_right = i if rightToCenter > maxRightToCenter else max_i_right
        maxRightToCenter = max(rightToCenter, maxRightToCenter)

    maxMiddle = (max_i_left, max_i_right, maxLeftToCenter + maxRightToCenter)

    return max([maxLeft, maxRight, maxMiddle], key=lambda x: x[2])


def loadTickerSymbols(file):
    '''Load in a file of edges'''

    sym_dict = defaultdict(str)
    with open(file, 'r') as f:
        for line in f:
            sym, name, *_ = line.split(",")
            sym_dict[sym.strip('"')] = name.strip('"')
    return sym_dict

def main():
    df = pd.read_csv('prices-split-adjusted.csv')
    df = df.pivot(columns='date', index='symbol', values='close')
    df.fillna(0, inplace=True)
    df_diff = df.diff(axis=1)
    df_diff.fillna(0, inplace=True)

    print("Test DAC algorithm with AAPL:")
    r = max_profit_DAC(df_diff.loc['AAPL'])
    print(f"AAPL profit: buy on day {r[0]} and sell on day {r[1]} for profit of {r[2]}\n")

    df['max_profit'] = df_diff.apply(max_profit_DAC, axis=1)
    df[['buy_i','sell_i','profit']] = df['max_profit'].to_list()
    df.drop('max_profit', axis=1, inplace=True)

    # Type cast to int and use to add buy date and sell date
    df['buy_i'] = df['buy_i'].astype('int')
    df['sell_i'] = df['sell_i'].astype('int')
    df['buy_date'] = df.columns[df['buy_i']]
    df['sell_date'] = df.columns[df['sell_i']]
    df['profit'] = df['profit'].astype('float')

    df = df.sort_values(by='profit', ascending=False)
    print("The top 5 stocks for maximum profit:")
    print(df['profit'].head(5), "\n")

    sym_dict = loadTickerSymbols("securities.csv")
    df['name'] = df.index.map(sym_dict)

    top = df.iloc[0]
    print("For best profit, buy stock in \"{}\" on {} and sell on {} for a profit of ${:.2f}".format(
        top['name'], top['buy_date'], top['sell_date'], top['profit']))

    # For best profit, buy stock in "Priceline.com Inc" on 2010-06-10 and sell on 2016-11-08 for a profit of $1402.94

if __name__ == "__main__":
    main()
