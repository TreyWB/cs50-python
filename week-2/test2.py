orig = "firstNamePreferredTest"
chars = ["N", "P", "T"]

for char in chars:
    split = orig.split(char)
    scored = split[0] + "_" + char + split[1]
    print(scored)