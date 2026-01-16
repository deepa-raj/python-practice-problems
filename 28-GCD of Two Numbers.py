a = 12
b = 18

gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
#
# print("GCD:", gcd)



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# → gcd(18, 12)
# → gcd(12, 6)
# → gcd(6, 0)
# → 6

print(gcd(a, b))