num = [1, 2, 4, 6, 3]
max = num[0]

for i in range(1, len(num)):
    if num[i] > max:
        max = num[i]

print(max)
