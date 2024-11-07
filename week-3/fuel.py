def main():
    # If error occurs, we reprompt by calling get_fraction() again
    # If try succeeds, move on to calc_fuel() & break to stop reprompting
    while True:
        try:
            x, y = get_fraction()
            percent = round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            calc_fuel(percent)
            break
        
    
def get_fraction():
    # Splits user input i.e. '1/5' to ['1', '5']
    fraction = input("Fraction: ")
    splits = fraction.split("/")
    
    x = int(splits[0])
    y = int(splits[1])
    
    # Raise error to avoid dividing by 0
    if x > y or y == 0:
        raise ValueError
    else:
        return x, y

def calc_fuel(percent):
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

main()