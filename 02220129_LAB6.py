def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if a > b:
            if b > c:
                return mid
            elif a > c:
                return high
            else:
                return low
        else:
            if a > c:
                return low
            elif b > c:
                return high
            else:
                return mid

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot_index = median_of_three(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps += 1

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

    original_list = arr.copy()
    quick_sort_recursive(0, len(arr) - 1)
    return original_list, arr, comparisons, swaps


# Example usage
original = [38, 27, 43, 3, 9, 82, 10]
original_list, sorted_list, comparisons, swaps = quick_sort(original.copy())

print("Original List:", original_list)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
