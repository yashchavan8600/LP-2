# Depth First Search
from collections import deque

# --- Algorithm Definitions ---
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Breadth First Search
def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    vertex = queue.popleft()
    print(vertex, end=" ")
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(graph, queue, visited)

# --- User Input Graph ---
graph = {}

n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input(f"Enter neighbors of {vertex} (space separated): ").split()
    graph[vertex] = neighbors

start_node = input("Enter starting node: ")

# --- Execution ---
print(f"\nStarting traversal from vertex: {start_node}")
print("-" * 30)

print("DFS Recursive Path:")
dfs_recursive(graph, start_node)

print("\n\nBFS Recursive Path:")

q = deque([start_node])
v = {start_node}

bfs_recursive(graph, q, v)
print()