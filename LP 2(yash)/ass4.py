# N-Queens Problem
"""
global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end='')
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQUtil(board, col + 1) == True:
                return True

            board[i][col] = 0

    return False

def solveNQ():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

solveNQ()
"""
# Graph coloring using greedy approach
"""
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

node = "abcdef"

# Count degree of all nodes
degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))

# Initialize color dictionary
colorDict = {}
for i in range(len(G)):
    colorDict[node[i]] = ["Blue", "Red", "Yellow", "Green"]

sortedNode = []
indeks = []

# Selection sort based on degree
for i in range(len(degree)):
    max_val = -1
    idx = -1
    for j in range(len(degree)):
        if j not in indeks:
            if degree[j] > max_val:
                max_val = degree[j]
                idx = j
    indeks.append(idx)
    sortedNode.append(node[idx])

# Main coloring process
theSolution = {}

for n in sortedNode:
    setTheColor = colorDict[n]
    theSolution[n] = setTheColor[0]

    adjacentNode = G[node.index(n)]

    for j in range(len(adjacentNode)):
        if adjacentNode[j] == 1 and (setTheColor[0] in colorDict[node[j]]):
            colorDict[node[j]].remove(setTheColor[0])

# Print the solution
for key, value in sorted(theSolution.items()):
    print("Node", key, "=", value)
"""

