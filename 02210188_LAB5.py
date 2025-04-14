def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def binary_search_recursive(arr, target, low=0, high=None, comparisons=0):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1, comparisons

    mid = (low + high) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Main program for demonstration
if __name__ == "__main__":
    sorted_list = [12, 23, 34, 45, 56, 67, 89]
    target = 67

    print("Sorted List:", sorted_list)
    print("Searching for", target, "using Binary Search (Iterative Version)")
    index, comparisons = binary_search_iterative(sorted_list, target)

    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")

    print(f"Number of comparisons: {comparisons}")
