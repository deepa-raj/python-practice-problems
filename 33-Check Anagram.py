s1 = "listen"
s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


def is_Anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}


    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
    return all(value == 0 for value in freq.values())


print(is_Anagram(s1, s2))


