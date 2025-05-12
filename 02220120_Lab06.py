def merge_sort(arr):
    comparisons = 3
    accesses = 2

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons += 1                    # One comparison
            accesses += 2                       # Access left[i] and right[j]

            if left[i] <= right[j]:
                result.append(left[i])
                accesses += 1                   # Appending = one access
                i += 1
            else:
                result.append(right[j])
                accesses += 1                   # Appending = one access
                j += 1

        while i < len(left):
            result.append(left[i])
            accesses += 1                       # Appending = one access
            i += 1

        while j < len(right):
            result.append(right[j])
            accesses += 1                       # Appending = one access
            j += 1

        return result

    def sort(subarray):
        if len(subarray) <= 1:
            return subarray
        mid = len(subarray) // 2
        left = sort(subarray[:mid])
        right = sort(subarray[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, comparisons, accesses

# Test the function
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, num_comparisons, num_accesses = merge_sort(original_list)
print("Original list : " , original_list)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", num_comparisons)
print("Number of array accesses:", num_accesses)
