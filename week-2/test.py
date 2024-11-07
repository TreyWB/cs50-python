orig = "firstNamePreferredTest"

# # Save char to split on
# char = orig[5].lower()

# # Split on capitalized char
# split = orig.split(orig[5])

# # Add splits + underscores
# added = split[0] + "_" + char + split[1]





# print("org =", orig)
# print("char =", char)
# print("split =", split)
# print("split of 1 =", split[0])
# print("added =", added)

chars = []

for i in orig:
    if i.isupper():
        chars.append(i)
       
       
print(chars)