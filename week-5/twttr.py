def main():
    original_string = input("Input: ")

    output = shorten(original_string)

    print("Output:", output)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    new_string = ""
    
    for c in word:
        if c not in vowels:
            new_string += c

    return new_string


if __name__ == "__main__":
    main()