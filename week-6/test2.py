name = "Potter, Harry"

modified = []

split_names = name.split(",", 1)

last = split_names[0]
first = split_names[1].lstrip()

modified.append({"last": last, "first": first})

print(modified)