import heapq

def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0

    pq = [(0, start_node)]
    predecessors = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors


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

start = input("Enter starting node: ")


# --- Execution ---
min_distances, path_tree = dijkstra(graph, start)

print("Shortest distances from", start)
for node, dist in min_distances.items():
    print(f"{node} : {dist}")

print("\nPredecessor tree:")
for node, parent in path_tree.items():
    print(f"{node} <- {parent}")

