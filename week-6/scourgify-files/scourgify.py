import sys
import csv

def main():
    param_check = validate_arguments()
    if param_check != None:
        sys.exit(param_check)

    students = []
    modified_students = []
    
    students, error = read_file(students)
    if error != None:
        sys.exit(error)

    modified_students = modify_data(students, modified_students)

    successful = write_new_file(modified_students)

    if successful == True:
        print(f"\nModification successful. Open {sys.argv[2]} to view results.")
    else:
        print(f"\nError writing to {sys.argv[2]}")


def read_file(students):
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        if isinstance(e, FileNotFoundError):
            error = f"\nFile not found. Try specifying absolute/path/to/file.csv"
            return None, error

    return students, None


def modify_data(original, modified):
    for entry in original:
        split_names = entry["name"].split(",", 1)

        last = split_names[0]
        first = split_names[1].lstrip()
        house = entry["house"]

        modified.append({"first": first, "last": last, "house": house})

    return modified

def write_new_file(modified_students):
    fields = ["first", "last", "house"]

    try:
        with open(f"{sys.argv[2]}", "w") as file:
            writer = csv.DictWriter(file, fieldnames=fields)

            writer.writeheader()

            writer.writerows(modified_students)
    except (PermissionError, IOError) as e:
        return False

    return True


def validate_arguments():
    if len(sys.argv) < 2:
        return f"Too few command-line arguments"
    elif len(sys.argv) > 3:
        return f"Too many command-line arguments"

    try:
        input_file_name, input_file_extension = sys.argv[1].split(".", 1)
        output_file_name, output_file_extension = sys.argv[2].split(".", 1)
    except (IndexError, TypeError) as e:
        return f"Too few command-line arguments"

    if input_file_extension != "csv" or output_file_extension != "csv":
        return f"Not a CSV File"

    return None


if __name__ == "__main__":
    main()