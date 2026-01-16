
# Remove all spaces
# s = "Hello world"
# res = s.replace(" ", "")


# Remove leading and trailing spaces
# s = "   Hello World   "
# res = s.strip()
# # res = s.lstrip()
# # res = s.rstrip()


# Remove multiple spaces between words
# s = "Hello    World    Python"
# res = " ".join(s.split())


# Remove spaces without using built-in function(loop logic)
s = "Hello World"
res = ""
for ch in s:
    if ch != " ":
        res += ch

print(res)