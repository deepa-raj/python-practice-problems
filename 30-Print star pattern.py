
n = 5

# # Basic pattern
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# # Right-angled triangle (increasing)
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# # Right-angled triangle (decreasing)
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# # Pyramid pattern
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("* " * i)


# # inverted pyramid pattern
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)


# # Full pyramid
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2*i - 1))


# Diamond pattern
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
