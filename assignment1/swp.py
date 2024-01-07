#!/usr/bin/env python3

from collections import defaultdict, deque
import sys

class MyQueue():
    """A simple Queue Class """

    def __init__(self, vals = None):
        self.Q = deque()
        if type(vals) == list:
            self.Q.extend(vals)
        if type(vals) == int:
            self.Q.append(vals)

    def __str__(self):
        if self.empty():
            return "Queue: Empty"
        else:
            return f"Queue: " + str(self.Q)

    def __iter__(self):
        return iter(self.Q)

    def enqueue(self, i):
        if type(i) == int:
            self.Q.append(i)
        elif type(i) == list:
            self.Q.extend(i)

    def dequeue(self):
        if self.empty():
            return None
        return self.Q.popleft()

    def empty(self):
        return False if self.Q else True


def loadGraph(edgeFile):
    '''Load in a file of edges'''

    adj_dict = defaultdict(list)
    with open(edgeFile, 'r') as f:
        for edge in f:
            A, B = edge.split(" ")
            A, B = int(A), int(B)
            adj_dict[A].append(B)
            adj_dict[B].append(A)
    return adj_dict


def BFS(G, s):
    """BFS Algorithm where G is an Graph represented
    by an adjaceny list and s is the starting vertex"""
    Q = MyQueue(s)
    d = {} # Dict of distances
    d[s] = 0 # Distance to starting node is 0
    while not Q.empty():
        v = Q.dequeue()
        for i in G[v]:
            # Examine vertex if not already in distance dict
            if not i in d:
                d[i] = d[v] + 1
                Q.enqueue(i)
    return d


def distanceDistribution(G):
    dist_counts = defaultdict(int)
    # Use size and counter to keep track of progress
    size = len(G)
    cnt = 0
    for v in G:
        # Update progress
        cnt += 1
        pct = cnt / size
        drawProgressBar(pct)

        d = BFS(G, v)
        del d[v] # Remove 0 distance entry
        for dist in d.values():
            dist_counts[dist] += 1

    # Convert to precentage
    total = sum(dist_counts.values())
    for k, v in dist_counts.items():
        dist_counts[k] = (v / total) * 100
    return dist_counts


def drawProgressBar(percent, barLen = 40):
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()


def main():
    #G = loadGraph("small.txt")
    G = loadGraph("edges.txt")

    print("Test run of BFS starting at 1:")
    d = BFS(G, 1)
    print(d)

    dists = distanceDistribution(G)
    print("\nDistribution of distances in G:")
    for k, v in dists.items():
        print(f"\t{k}: {v:.2f}")

# Distribution of distances in G:
#	1: 1.08
#	2: 16.65
#	3: 24.41
#	4: 35.94
#	5: 15.73
#	6: 4.15
#	7: 1.93
#	8: 0.10
#
# This network absolutely satisfies the small world problem as only 2% of
# distances in the network are greater than 6 degrees, and there is no distance
# greater than 8.

if __name__ == "__main__":
    main()
