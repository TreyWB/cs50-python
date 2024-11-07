ciphertext = "Otkz D zvmizy v amzz kjdio! di ocz wjs wzgjr"

for key in range(1, 26):
    print(f"Key {key}:", end=" ")

    for char in ciphertext:
        if char.isalpha():
            uni_dec = ord(char)

            if uni_dec >= 65 and uni_dec <= 90:
                if ord(char) + key > 90:
                    test = ord(char) + key - 26
                else:
                    test = ord(char) + key
            elif uni_dec >= 97 and uni_dec <= 122:
                if ord(char) + key > 122:
                    test = ord(char) + key - 26
                else:
                    test = ord(char) + key
        else:
            test = ord(char)

        print(chr(test), end="")

    print()