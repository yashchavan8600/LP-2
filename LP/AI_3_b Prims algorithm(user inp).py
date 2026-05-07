import heapq

def prims_algorithm(graph, start_node):
    mst = []
    visited = set()
    edges_heap = []

    visited.add(start_node)

    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges_heap, (weight, start_node, neighbor))

    total_cost = 0

    while edges_heap:
        cost, u, v = heapq.heappop(edges_heap)

        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, cost))
        total_cost += cost

        for neighbor, weight in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(edges_heap, (weight, v, neighbor))

    return mst, total_cost


# --- User Input ---
graph = {}

n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = input("Enter vertex: ")
    neighbors = {}

    m = int(input(f"Enter number of neighbors for {vertex}: "))
    for _ in range(m):
        neigh = input("Enter neighbor: ")
        weight = int(input(f"Enter weight of edge {vertex}-{neigh}: "))
        neighbors[neigh] = weight

    graph[vertex] = neighbors

start = input("Enter starting vertex: ")


# --- Execution ---
mst_result, total_weight = prims_algorithm(graph, start)

print(f"\nMinimum Spanning Tree starting from {start}:")
for u, v, weight in mst_result:
    print(f"Edge: {u} - {v} | Cost: {weight}")

print(f"\nTotal MST Weight: {total_weight}")