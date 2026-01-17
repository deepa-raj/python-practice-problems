s = "Python"
vowel = 0
consonent = 0

# To find consonent in this string
consonent = 0
for ch in s.lower():
    if "a" <= ch <= "z":
        if ch in "aeiou":
            vowel += 1
        else:
            consonent += 1
print(vowel)
print(consonent)