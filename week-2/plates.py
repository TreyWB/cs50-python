def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for c in s:
            d = c -1
            if s[d:c].isalpha():
                return False
            else:
                return True

main()