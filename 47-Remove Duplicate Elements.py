arr = [1, 2, 2, 3, 4, 4, 5]


# # Using loop
# unique = []
# for i in arr:
#     if i not in unique:
#         unique.append(i)
#
# print(unique)


# # Using set()
# unique = list(set(arr))
# print(unique)


# Preserve order
unique = []
seen = set()

for i in arr:
    if i not in seen:
        unique.append(i)
        seen.add(i)
print(unique)

