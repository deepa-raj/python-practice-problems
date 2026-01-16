num = [5, 3, 2, 4, 1]
min = num[0]

for i in range(1, len(num)):
    if num[i] < min:
        min = num[i]


print(min)