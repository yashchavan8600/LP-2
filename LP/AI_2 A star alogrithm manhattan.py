import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def a_star(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for new_pos in neighbors:
            node_pos = (
                current_node.position[0] + new_pos[0],
                current_node.position[1] + new_pos[1]
            )

            if (node_pos[0] < 0 or node_pos[0] >= len(grid) or
                node_pos[1] < 0 or node_pos[1] >= len(grid[0])):
                continue

            if grid[node_pos[0]][node_pos[1]] != 0:
                continue

            if node_pos in closed_list:
                continue

            neighbor_node = Node(node_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(open_node.position == neighbor_node.position and
                   neighbor_node.g > open_node.g for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None


# --- User Input ---
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []
print("Enter grid row by row (0 = free, 1 = blocked):")
for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

start = tuple(map(int, input("Enter start position (row col): ").split()))
end = tuple(map(int, input("Enter end position (row col): ").split()))

# --- Execution ---
path = a_star(grid, start, end)

print(f"Start: {start} | End: {end}")
print("Path found:", path if path else "No path available")

#input no of rows 3
#no of col 3
#grid row by row
# 0 1 0
# 0 0 0
# 1 0 0
# start posi 0 0
# end posi 2 2 