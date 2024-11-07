def main():
    original_string = input("Input: ")
    
    output = remove_vowel(original_string)

    print("Output:", output)

def remove_vowel(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    new_string = ""
    
    for c in string:
        if c not in vowels:
            new_string = new_string + c

    return new_string
    
main()