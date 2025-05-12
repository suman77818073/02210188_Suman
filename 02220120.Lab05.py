def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2

        comparisons += 1  # Comparing arr[mid] with target
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def binary_search_recursive(arr, target, left=0, right=None, comparisons=0):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1, comparisons

    comparisons += 1
    mid = (left + right) // 2

    comparisons += 1  # Comparing arr[mid] with target
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)


# Example usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)

# Iterative search
print(f"\nSearching for {target} using Iterative Binary Search...")
index_iter, comparisons_iter = binary_search_iterative(arr, target)
print("Found at index:" if index_iter != -1 else "Not found.", index_iter)
print("Number of comparisons:", comparisons_iter)

# Recursive search
print(f"\nSearching for {target} using Recursive Binary Search...")
index_rec, comparisons_rec = binary_search_recursive(arr, target)
print("Found at index:" if index_rec != -1 else "Not found.", index_rec)
print("Number of comparisons:", comparisons_rec)
