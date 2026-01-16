num = 6
res = 0

# method 1
# for i in range(1, num):
#     if num % i == 0:
#         res += i
#
# if res == num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")
# -----------------------------------------

# method 2


def is_perfect(num):
    if num <= 1:
        return False

    div_sum = 1
    i = 2

    while i * i <= num:
        if num % i == 0:
            div_sum += i

            if i != num // i:
                div_sum += num // i
        i += 1

    return div_sum == num


if is_perfect(num):
    print("Perfect")
else:
    print("Not Perfect")
