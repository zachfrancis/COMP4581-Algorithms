#!/usr/bin/env python3

# Finds ALL ways to place n nonattacking queens on a n x n board
# NOTE: State[i] is the row for the queen on Column i
# NOTE: There are solutions for n > 3

# Stack ADT with list implementation from Lab 5
class MyStack(object):
    def __init__(self, type):
        self.elemType = type
        self.state = []

    def __str__(self):
        return str(self.state)

    def empty(self):
        return len(self.state) == 0

    def push(self, elem):
        assert type(elem) == self.elemType
        self.state.append(elem)

    def pop(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()

    def top(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def nQueens(n):
    # Each state will include only the queens that have been placed so far
    initialState = []

    s = MyStack(list)
    s.push(initialState)

    # While we still have states to explore
    while not s.empty():
        currentState = s.pop()
        currentCol = len(currentState)

        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
            # Produce the state's children (if they are feasible)
            # Note children are produced backward so they come off the
            # stack later left to right
            for currentRow in range(n, 0, -1):
                # Check horizontal and both diagonals of previous queens
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or \
                    abs(currentState[previousCol] - currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState)  # Push child onto data structure

def graphColoring(graph, colors):
    n = len(graph)

    s = MyStack(list)
    s.push([])

    while not s.empty():
        currentColors = s.pop()
        currentNode = len(currentColors)

        if len(currentColors) == n:
            return currentColors

        for color in colors:
            feasible = True
            for prevNode in range(currentNode):
                if graph[prevNode][currentNode]:
                    if currentColors[prevNode] == color:
                        feasible = False
                        break
            if feasible:
                newColors = currentColors.copy()
                newColors.append(color)
                s.push(newColors)



# Testing code (check 4, 5, 6, 7)
#for n in range(4, 8):
#    nQueens(n)

graph = [[False, True, False, False, False, True],
         [True, False, True, False, False, True],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True],
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']
r = graphColoring(graph, colors)
print(r)
# Output: ['b', 'g', 'b', 'r', 'g', 'r']
