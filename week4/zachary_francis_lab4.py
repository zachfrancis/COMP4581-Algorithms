#!/usr/bin/env python3


def cPairDist(points):
    print(f"cPairDist called with {points}")
    return recCPairDist(sorted(points))


def recCPairDist(points):
    print(f"recCPairDist called with {points}")
    # Base Cases are lists of length 2 and 3
    if len(points) == 2:
        return abs(points[1] - points[0])
    elif len(points) == 3:
        left = abs(points[1] - points[0])
        right = abs(points[2] - points[1])
        return min(left, right)

    # Divide and recurse
    mid_i = len(points) // 2
    left = recCPairDist(points[:mid_i])
    right = recCPairDist(points[mid_i:])
    mid = abs(points[mid_i] - points[mid_i - 1])
    return min(left, right, mid)


def main():
    p1 = [7, 4, 12, 14, 2, 10, 16, 6]
    p2 = [7, 4, 12, 14, 2, 10, 16, 5]
    p3 = [14, 8, 2, 6, 3, 10, 12]

    print(cPairDist(p1))
    print(cPairDist(p2))
    print(cPairDist(p3))


if __name__ == "__main__":
    main()
