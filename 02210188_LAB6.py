def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(low, high):
        mid = (low + high) // 2
        trio = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        trio.sort(key=lambda x: x[0])
        return trio[1][1]  # Return index of the median value

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot_index = median_of_three(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        swaps += 1

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    # Call the recursive function
    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps

# Example usage:
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comparisons, swaps = quick_sort(original_list.copy())

print("Original List:", original_list)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
