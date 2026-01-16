num = [2, 3, 1, 4, 5, 7, 8]
count = 0

for i in range(len(num)):
    if num[i] % 2 != 0:
        count += 1
print(count)
