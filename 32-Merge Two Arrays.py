# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]

# # Simple way - unsorted
# merged = arr1 + arr2
# print(merged)


# # Using loop
# merged = []
#
# for num in arr1:
#     merged.append(num)
#
# for num in arr2:
#     merged.append(num)
#
# print(merged)


# Merge two sorted arrays
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]


def merged_sorted(arr1, arr2):
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged


print(merged_sorted(arr1, arr2))


