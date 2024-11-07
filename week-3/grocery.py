def main():
    # Initialize list, so get_list() can append to it
    groceries = []

    # Loop to reprompt continuously until EOFError (Ctrl + D) occurs
    while True:
        try:
            groceries = get_list(groceries)
        except EOFError:
            display_list(groceries)
            break


def get_list(groceries):
    item = (input(""))

    # Can also type "end" or "done" to end prompt loop
    if item == "done" or item == "end":
        raise EOFError

    # Add requested item to list
    groceries.append(item.upper())
    return groceries


def display_list(groceries):
    # Initialize dictionary to use in for loop
    unique_list = {}

    # Sort list, instead of dictionary, because it's easier
    groceries = sorted(groceries)

    # Loops through list, checking if item is already in our unique dictionary
    for grocery in groceries:
        # Add item to dictionary with value "1", if not already in there
        if grocery not in unique_list:
            unique_list[f"{grocery}"] = "1"
        # Increase item's value by 1, if it's already in dictionary
        elif grocery in unique_list:
            count = int(unique_list[grocery]) + 1
            unique_list[f"{grocery}"] = str(count)

    # Print blank line between user input & grocery list output
    print("")
    # Print item's value from dictionary first, then item name
    # Do this in a loop so each item will be printed on a seperate line
    for item in unique_list:
        print(f"{unique_list[item]} {item}")

main()