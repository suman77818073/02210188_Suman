def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0  # Start at 0 and increment only when a comparison is made

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1  # One comparison for each loop iteration

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


# Example usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search...")
index, comparisons = binary_search_iterative(arr, target)

if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found.")

print("Number of comparisons:", comparisons)