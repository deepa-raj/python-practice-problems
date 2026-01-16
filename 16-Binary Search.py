num = [1, 2, 4, 6, 33, 21]
target = 33

num.sort()

def binary_search(num, target):
    low = 0
    high = len(num) - 1

    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

res = binary_search(num, target)


if res != -1:
    print("Found")
else:
    print("Not Found")