s = "Python is easy to learn"


# Using split()
# word = s.split()
# count = len(word)
# print(count)


# Without using split()
in_word = False
count = 0

for ch in s:
    if ch != " " and not in_word:
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print(count)

