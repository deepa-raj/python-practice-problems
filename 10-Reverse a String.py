
s = "hello"


# method 1 - slicing
# print(s[::-1])


# method 2 - for loop
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)


# method 3 - while loop using indexing
# rev = ""
# i = len(s) - 1
# while i >= 0:
#     rev += s[i]
#     i -= 1
# print(rev)


# method 4 - list + reverse
# rev = ""
# char = list(s)
# char.reverse()
# rev = "".join(char)  # list element to string
# print(rev)


# method 5 - recursion
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return reverse_string(s[1:]) + s[0]
#
# 
# print(reverse_string(s))
