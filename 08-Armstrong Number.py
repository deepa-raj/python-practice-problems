num = 153

temp = num
n = num

total = 0
count = 0
while num > 0:
    count += 1
    num = num // 10

while temp > 0:
    digit = temp % 10
    total += digit ** count
    temp //= 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")