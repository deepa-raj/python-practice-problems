arr = [10, 20, 30, 40, 50]
target = 30

# index = -1
# # Uisng loop
# for i in range(len(arr)):
#     if arr[i] == target:
#         index = i
#         break
#
# if index != -1:
#     print("Element found at index:", index)
# else:
#     print("Element not found")


# # Using index() (Python built-in) -> Works only for first occurrence
# if target in arr:
#     print(arr.index(target))
# else:
#     print("Not Found")


# Using enumerate()
for i, val in enumerate(arr):
    if val == target:
        print("Index:", i)
        break
