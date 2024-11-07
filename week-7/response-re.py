import re
import sys

def main():
    print(validate_email(input("What's Your Email? ")))
    
def validate_email(e):
    if re.search("^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", e, re.IGNORECASE):
        return "Valid"
    else:
        return "Invalid"
        
        
        
if __name__ == "__main__":
    main()