def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            if not (cols[col] or diag1[row + col] or diag2[row - col + n - 1]):
                board[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

                backtrack(row + 1)

                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for row in solution:
        line = ["Q" if i == row else "." for i in range(n)]
        print(" ".join(line))
    print("\n")


# --- User Input ---
n_size = int(input("Enter value of N (number of queens): "))

results = solve_n_queens(n_size)

print(f"Found {len(results)} solutions for {n_size}-Queens:\n")

for sol in results:
    print_board(sol)