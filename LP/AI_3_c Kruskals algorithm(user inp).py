class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


def kruskals_algorithm(vertices, edges):
    mst = []
    sorted_edges = sorted(edges, key=lambda item: item[2])
    uf = UnionFind(vertices)
    total_cost = 0

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# --- User Input ---
n = int(input("Enter number of vertices: "))
nodes = []

for _ in range(n):
    node = input("Enter vertex: ")
    nodes.append(node)

e = int(input("Enter number of edges: "))
graph_edges = []

for _ in range(e):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")
    w = int(input(f"Enter weight for edge {u}-{v}: "))
    graph_edges.append((u, v, w))


# --- Execution ---
mst_result, total_weight = kruskals_algorithm(nodes, graph_edges)

print("Minimum Spanning Tree:")
for u, v, w in mst_result:
    print(f"Edge: {u} - {v} | Cost: {w}")

print("Total Cost:", total_weight)