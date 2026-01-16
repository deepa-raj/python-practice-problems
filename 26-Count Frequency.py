arr = [1, 2, 3, 2, 4, 1, 5, 3]

# Using dictionary
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
#
# duplicates = [key for key, value in freq.items() if value > 1]
# print(freq)


# Using get()
# freq = {}
# for num in arr:
#     freq[num] = freq.get(num, 0) + 1
# print(freq)


# Count freq of character in a string
# s = "programming"
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)


# Count freq of words in a sentence
s = "python is easy and python is powerful"
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
