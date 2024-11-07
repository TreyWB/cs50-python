# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         pass
#     else:
#         break

# print("x = ", x)
def main():
    try:
        fraction = input("Fraction: ")
        splits = fraction.split('/')
    except ValueError as e:
        print("No '/' found")
    else:
        print_values(splits)

def print_values(splits):
    x = int(splits[0])
    y = int(splits[1])

    return ValueError
    # print("x =", x)
    # print("y =", y)

main()
# for i in fraction:
#     if i == "/":
#         splits = split(fraction[i])
#         print(splits)
#         break

