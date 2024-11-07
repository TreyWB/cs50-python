def main():
    fraction = input("Fraction: ")

    while True:
        try:
            percent = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            output = gauge(percent)
            break

    print(output)


def convert(fraction):
    splits = fraction.split("/")
    
    x = int(splits[0])
    y = int(splits[1])
    
    if x > y or y == 0:
        raise ZeroDivisionError
    
    percent = round((x / y) * 100)

    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()