def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- User Input ---
data = list(map(int, input("Enter elements (space separated): ").split()))

print(f"Original array: {data}")

sorted_data = selection_sort(data.copy())

print(f"Sorted array: {sorted_data}")