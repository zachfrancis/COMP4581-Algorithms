#!/usr/bin/env python3

# Dijkstra's shortest path greedy algorithm
# Find the min priority vertex from the list of given vertices
# Each vertex in the form of a list with priority as the first
# element returns the min vertex and removes it from the list
def extractMin(verts):
    minIndex = 0
    for v in range(1, len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)

# Dijkstra's shortest path algorithm
def shortest(g):

    # Create a list of vertices and thier current shortest distances
    # from vertex 0
    # [verNum, dist]
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    # Start at vertex 0 - it had a current shortest distance of 0
    vertsToProcess[0][1] = 0

    # Start with an empty list of processed edges
    vertsProcessed = []

    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess)
        vertsProcessed.append(u)
        # print("to process:", vertsToProcess)
        # print(" processed:", vertsProcessed)

        # Examine all potential verts remaining
        for v in vertsToProcess:
            # Only care about the ones that are adjacent to u
            if g[u[0]][v[0]] > 0:
                # Update the distance if necessary
                if u[1] + g[u[0]][v[0]] < v[1]:
                    v[1] = u[1] + g[u[0]][v[0]]

    print(vertsProcessed)


# Prim's Minimum Spanning Tree Algorithm
def mst(g):
    vertsToProcess = [[i, float("inf")] for i in range(len(g))]
    mst = [[i, -1] for i in range(len(g))]

    vertsToProcess[0][1] = 0
    while vertsToProcess:
        u = extractMin(vertsToProcess)
        for v in vertsToProcess:
            # If Adjacent
            if g[u[0]][v[0]] > 0:
                # If adj dist is less than current min
                if g[u[0]][v[0]] < v[1]:
                    v[1] = g[u[0]][v[0]]
                    mst[v[0]][1] = u[0]
    return mst


graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9],
         [0, 12, 0, 6, 0, 0, 0, 0],
         [0, 5, 6, 0, 14, 8, 0, 0],
         [0, 0, 0, 14, 0, 3, 0, 0],
         [10, 0, 0, 8, 3, 0, 0, 0],
         [15, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0]]

print("Shortest Path Algorithm:")
shortest(graph)
print("Minimum Spanning Tree:")
print(mst(graph))
# Output: [[0, -1], [1, 0], [2, 3], [3, 1], [4, 5], [5, 3], [6, 0], [7, 1]]