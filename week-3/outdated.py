def main():
    # Use while loop to continuously reprompt if error occurs
    while True:
        try:
            month, day, year = get_date()
        except (ValueError, AttributeError, TypeError, UnboundLocalError) as e:
            pass
        try:
            convert_date(month, day, year)
            break
        except (ValueError, AttributeError, TypeError, UnboundLocalError) as e:
            pass
    
def get_date():
    me_date = input("Date: ")
    
    # Different split methods, depending on user inputted date; i.e. "January 31, 2023" or "1/31/2023"
    if "," in me_date:
        splits = me_date.split(" ", 2)
    elif "/" in me_date:
        splits = me_date.split("/", 2)
    else:
        raise ValueError

    month = splits[0]
    day = splits[1]
    year = splits[2]

    # If there's a trailing comma, we remove it
    if "," in day:
        day = day.replace(",", "")
    
    # If user provided month in word form, we convert it using calendar_to_digit()
    if month.isalpha():
        month = calendar_to_digit(month.lower())
       
    # Checks to ensure user provided valid date
    if int(month) > 12 or int(day) > 31 or int(year) < 1:
        raise ValueError
    
    return month, day, year
    
def calendar_to_digit(month):
    calendar_months = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12"
    }
    
    for unit in calendar_months:
        if month == unit:
            # If user input month is in calendar_months dictionary, we replace it with corresponding month number
            month = calendar_months[f"{unit}"]
            return month
    
    raise ValueError

def convert_date(month, day, year):
    len_month = len(month)
    len_day = len(day)
    len_year = len(year)

    # If user provided single-digit dates, i.e. M/D/YYYY, we prepend 0, converting it to MM/DD/YYYY
    if len_month == 1:
        month = "0" + month
    elif len_month == 2:
        pass
    else:
        raise ValueError

    # If user provided single-digit dates, i.e. M/D/YYYY, we prepend 0, converting it to MM/DD/YYYY
    if len_day == 1:
        day = "0" + day
    elif len_day == 2:
        pass
    else:
        raise ValueError
    
    # If user provided 2 digit year, we error and reprompt
    if len_year != 4:
        raise ValueError
    
    # Print date in ISO8601 format
    print(f"{year}-{month}-{day}")

main()