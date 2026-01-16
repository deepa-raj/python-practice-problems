num = [2, 3, 1, 4, 5, 7, 8]


def second_largest(num):
    if len(num) < 2:
        return None

    largest = second = float("-inf")

    for n in num:
        if n > largest:
            second = largest
            largest = n
        elif n != largest and n > second:
            second = n
    if second == float("-inf"):
        return None

    return second

res = second_largest(num)

if res is not None:
    print("Second Largest: ",res)
else:
    print("Second largest doesn't exist")