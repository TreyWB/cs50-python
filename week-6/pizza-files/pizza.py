import sys
from tabulate import tabulate
import csv
from param_check import check_parameter_file

param_check = check_parameter_file(2, 2, "csv", "CSV")

if param_check != None:
    sys.exit(param_check)

menu_items = []

try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            menu_items.append(row)
        
except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    if isinstance(e, FileNotFoundError):
        sys.exit(f"\nFile does not exist")
    else:
        sys.exit(f"\nError opening file. Try providing absolute/path/to/file.csv")

print(tabulate(menu_items, headers="keys", tablefmt="grid"))

