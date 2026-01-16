arr = [1, 2, 3, 2, 4, 1, 5, 3]


# # Using Slicing
# arr = arr[::-1]
# print(arr)


# Using Two Pointers
start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)



