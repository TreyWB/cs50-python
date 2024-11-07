import sys

def check_parameter_file(min_parameters, max_parameters, extension_abbreviation, extension_full_name):
    if len(sys.argv) < min_parameters:
        return f"\nToo few command-line arguments"
    elif len(sys.argv) > max_parameters:
        return f"\nToo many command-line arguments"

    if "." not in sys.argv[1]:
        return f"\nNot a {extension_full_name} file"
    
    file_name, file_extension = sys.argv[1].split(".", 1)

    if "." in file_extension or file_extension != f"{extension_abbreviation}":
        return f"\nNot a {extension_full_name} file"

    try:
        if file_extension not in sys.argv[2]:
            return f"File extensions must be the same"
    except IndexError:
        pass

if __name__ == "__main__":
    check_parameter_file(2, 2, "csv", "CSV")