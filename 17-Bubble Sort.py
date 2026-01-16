num = [9, 5, 3, 1, 8, 4]
n = len(num)

for i in range(n):
    swapped = False

    for j in range(0, n-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            swapped = True
    if not swapped:
        break

print(num)