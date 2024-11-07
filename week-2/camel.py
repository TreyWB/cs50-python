import sys

def main():
    camel = input("camelCase: ")

    # Initialize storage for capitals
    caps = []
    caps = find_capitals(caps, camel)

    # Count modifications required
    count = len(caps)

    # Return user input if no changes required
    if count == 0:
        print("snake_case:", camel)
        sys.exit()

    # Split input & add underscores
    snake = add_underscore(caps, count, camel)

    print("snake_case:", snake.lower())

def find_capitals(caps, camel_case):
    for i in camel_case:
        if i.isupper():
            caps.append(i)

    return caps

def add_underscore(caps, count, camel):
    string = camel
    n = 0

    while n <= count:
        for cap in caps:
            # Split string at capital letter
            split = string.split(cap)

            # Add underscore before capital letter
            scored_split = split[0] + "_" + cap + split[1]

            # Remove capital letter from list
            caps.remove(cap)

            break

        # Save string with underscore added
        string = scored_split
        n += 1

    return string

main()