num = 6
power = 3

# # Using **
# print(num ** power)

# # Without **
# result = 1
# for i in range(power):
#     result = result * num
# print(result)


# Using recursion
def power_of_num(num, power):
    if power == 0:
        return 1
    return num * power_of_num(num, power-1)


print(power_of_num(num, power))

