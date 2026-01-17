
arr = [1, 2, 4, 5]
n = len(arr) + 1

# expected_sum = n * (n + 1) // 2
# actual_sum = sum(arr)
# missing = expected_sum - actual_sum
# print("Missing number: ", missing)


# expected_sum = 0
# for i in range(1, n + 1):
#     expected_sum += i
#
# actual_sum = 0
# for num in arr:
#     actual_sum += num
#
# print("Missing number:", expected_sum - actual_sum)


xor_all = 0
for i in range(1, n + 1):
    xor_all ^= i

xor_arr = 0
for num in arr:
    xor_arr ^= num

print("Missing number:", xor_all ^ xor_arr)

