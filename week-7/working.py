import re
import sys


def main():
    print(parse(input("Hours: ")))

def parse(t):
    matches = re.search(r"(\d\d?):?(\d\d)? (AM|PM) to (\d\d?):?(\d\d)? (AM|PM)", t, re.IGNORECASE)
    
    try:
        s_hr = matches.group(1)
        s_min = matches.group(2)
        s_dp = matches.group(3)

        end_hr = matches.group(4)
        end_min = matches.group(5)
        end_dp = matches.group(6)
    except (AttributeError, ValueError, TypeError):
        sys.exit("Improper Formatting")
    
    if s_min == None:
        s_min = "00"

    if end_min == None:
        end_min = "00"

    if int(s_min) > 59:
        sys.exit("Invalid Time")
    if int(end_min) > 59:
        sys.exit("Invalid Time")
    
    converted_time = convert(s_hr, s_min, s_dp, end_hr, end_min, end_dp)

    return converted_time

def convert(s_hr, s_min, s_dp, end_hr, end_min, end_dp):
    am_dict = {
        '12': '00',
        '1': '01',
        '2': '02',
        '3': '03',
        '4': '04',
        '5': '05',
        '6': '06',
        '7': '07',
        '8': '08',
        '9': '09',
        '10': '10',
        '11': '11'
    }
    
    pm_dict = {
        '12': '12',
        '1': '13',
        '2': '14',
        '3': '15',
        '4': '16',
        '5': '17',
        '6': '18',
        '7': '19',
        '8': '20',
        '9': '21',
        '10': '22',
        '11': '23'
    }
    
    if s_dp == "AM":
        new_s_hr = am_dict[s_hr]
    elif s_dp == "PM":
        new_s_hr = pm_dict[s_hr]
        
    if end_dp == "AM":
        new_end_hr = am_dict[end_hr]
    elif end_dp == "PM":
        new_end_hr = pm_dict[end_hr]
        
    new_start_time = f"{new_s_hr}:{s_min}"
    new_end_time = f"{new_end_hr}:{end_min}"
    
    time = f"{new_start_time} to {new_end_time}"

    return time


if __name__ == "__main__":
    main()