def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    
    if 6>= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for c in s:
            try:
                int(s[i])
            except ValueError:
                pass
            else:
                if s[i:].isdigit() and s[i] != "0":
                    return True
                else:
                    return False
            i += 1
    else:
        return False



if __name__ == "__main__":
    main()