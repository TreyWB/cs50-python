def main():
    time = input("What time is it? ")

    # Split time in 12:00 to "12" and "00" 
    whole, minutes = split_time(time)

    rounded_hours = round(calculate(whole, minutes),2)

    # Prints what meal is required
    meal_info(rounded_hours)

def split_time(time):
    split = time.split(":")
    
    # Get Hour float from user-supplied time
    whole = float(split[0]) 

    # Get Minutes float from user-supplied time
    minutes = float(split[1])

    return whole, minutes

def calculate(whole, minutes):
    # Convert "7:30" to "7.5"
    hours = whole + (minutes / 60)
    
    return hours

def meal_info(rounded_hours):
    if 7.00 <= rounded_hours <= 8.00:
        print("It's Breakfast Time!")
    elif 12.00 <= rounded_hours <= 13.00:
        print("It's Lunch Time!")
    elif 18.00 <= rounded_hours <= 19.00:
        print("It's Dinner Time!")
    else:
        print("Don't eat. Fat.")

main()