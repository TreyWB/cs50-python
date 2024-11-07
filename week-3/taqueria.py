def main():
    # Initialize variable for order_item()
    total = 0
    
    # Prompt & reprompt for desired item, break on EOFError (Ctrl + D) is equivalent to sys.exit()
    while True:
        try:
            total = order_item(total)
        except EOFError:
            break
        
def order_item(total):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    order = input("Item: ").title()
    
    # Other ways to end program
    if order == "End" or order == "Done":
        raise EOFError

    # Iterate over menu, if input matches take price and add to total
    for item in menu:
        if item == order:
            total += menu[item]
            print(f"Total: ${total:.2f}")
            return total

    # Need this or else typos return total as None
    return total
main()