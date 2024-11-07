fruits = ['apple', 'apple', 'banana']

# fruits.sort()

# length = len(fruits)

count = 1

# list = {}
unique = {}

# for i in range(0, length):
#     for fruit in fruits:
#         if fruit == fruits[i + 1]:
#             count += 1
#             print(f"{count} {fruits[i]}")
#         elif fruit != fruits[i + 1]:
#             print(f"1 {fruits[i]}")
#         i += 1
        
for fruit in fruits:
    if fruit not in unique:
        unique[f"{fruit}"] = "1"
        continue
    if fruit in unique:
        count += 1
        unique[f"{fruit}"] = str(count)

for item in unique:
    print(f"{unique[item]} {item}")