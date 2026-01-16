arr = [1, 2, 3, 2, 4, 1, 5, 3]


# # Using Nested loops
# duplicates = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in duplicates:
#             duplicates.append(arr[i])
# print("Duplicates: ", duplicates)


# Using set
# seen = set()
# duplicate = set()
#
# for num in arr:
#     if num in seen:
#         duplicate.add(num)
#     else:
#         seen.add(num)
# print(list(duplicate))


# Using dictionary
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

duplicates = [key for key, value in freq.items() if value > 1]
print(duplicates)