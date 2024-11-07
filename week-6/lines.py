import sys

def main():
    check_parameter()

    line_count = count_lines()

    print("Lines of Code:", line_count)

def check_parameter():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if "." not in sys.argv[1]:
        sys.exit("Not a python file")
    
    file_name, file_extension = sys.argv[1].split(".", 1)

    if "." in file_extension or file_extension != "py":
        sys.exit("Not a python file")

def count_lines():
    line_count = 0
    
    try:
        with open(f"{sys.argv[1]}") as file:
           lines = file.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        sys.exit("Error opening file. Try providing absolute/path/to/file.py")

    for line in lines:
        if line.isspace():
            continue
        elif "#" in line:
            continue
        else:
            line_count += 1
    
    return line_count



if __name__ == "__main__":
    main()