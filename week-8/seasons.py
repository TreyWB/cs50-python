import datetime
import sys
import re
import inflect

def get_input():
    dob = input("Date of Birth: ")

    main(dob)

def main(dob):
    user = User(dob)

    year, month, date = user.dob_info()
    
    output = user.calc_minutes(year, month, date)
    
    print(f"\n{output.capitalize()} minutes")
    

class User:
    current_date = datetime.datetime.now()
    
    def __init__(self, dob):
        self.dob = dob
        
    def dob_info(self):
        if matches := re.search(r"(\d\d\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])", self.dob):
            year = int(matches.group(1))
            month = int(matches.group(2))
            date = int(matches.group(3))
        else:
            sys.exit(f"\nInvalid date; Use format: YYYY-MM-DD")

        return (year, month, date)
    
    def calc_minutes(self, year, month, date):
        p = inflect.engine()
        
        dob_date = datetime.datetime(year, month, date)
        diff = self.current_date-dob_date

        minutes = diff.days * 24 * 60
        output = p.number_to_words(minutes, andword="")
        
        return output
    


if __name__ == "__main__":
    get_input()