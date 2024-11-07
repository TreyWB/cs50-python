import sys

def main():
    names = []
    while True:
        try:
            names = get_names(names)
        except (EOFError) as e:
            say_adieu(names)
            break

def get_names(names):
    names.append(input("Name: "))
    
    # Error if user pressed Enter instead of providing a name
    if "" in names:
        sys.exit("You cannot provide a blank name")
    
    return names

def say_adieu(names):
    # Inititalize variables to use in for loop
    line = "Adieu, adieu, to "
    i = 0

    for name in names:
        if i == 0:
            line = line + name
            i += 1

        elif i == 1:
            line = line + " and " + name
            i += 1

        elif i == 2:
            # Splice everything after contents of line variable
            names_from_line = line[17:]
            # Remove "and" between names, replace with a comma
            names_from_line = names_from_line.replace(" and", ",")
            # Reinitialize variable
            line = "Adieu, adieu, to "
            # Build line for printing
            line = line + names_from_line + ", and " + name

            i += 1

        else:
            # Splice everything after contents of line variable
            names_from_line = line[17:]
            # Remove "and" between names
            names_from_line = names_from_line.replace("and ", "")
            # Add current name to line
            names_from_line = names_from_line + "," + " and " + name
            # Reinitialize variable
            line = "Adieu, adieu, to "
            # Build line for printing
            line = line + names_from_line

            i += 1

    # Print finalized output
    print(f"\n{line}", end='')



if __name__ == "__main__":
    main()