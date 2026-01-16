num = 5


def is_prime(num):
    if num < 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

num = 29
print(f"Is {num} Prime: {is_prime(num)}")

