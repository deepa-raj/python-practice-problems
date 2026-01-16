
s = "malayalam"


# method 1 - slicing
# print(s[::-1])


# method 2 - for loop
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)
# if rev == s:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# method 3 - while loop using indexing
# rev = ""
# i = len(s) - 1
# while i >= 0:
#     rev += s[i]
#     i -= 1
# print(rev)
# if rev == s:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# method 4 - list + reverse
rev = ""
# char = list(s)
# char.reverse()
# rev = "".join(char)  # list element to string
# if rev == s:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# method 5 - recursion
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

rev = reverse_string(s)
if rev == s:
    print("Palindrome")
else:
    print("Not Palindrome")
