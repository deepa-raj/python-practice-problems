num = [1, 2, 4, 6, 33, 21]
target = 31


# found = False
# for i in range(0, len(num)):
#     if num[i] == target:
#         print("Element found")
#         found = True
#         break
# if not found:
#     print("Element not found")


# Using for-each loop
for index, value in enumerate(num):
    if value == target:
        print("Found")
        break
else:
    print("Not Found")
