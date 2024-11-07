from validator_collection import validators, errors
import sys

def main():
    print(validate_email(input("What's your email? ")))
    
def validate_email(e):
    if " " in e:
        return "Invalid"
    
    try:
        if validators.email(e):
            return "Valid"
        else:
            return "Invalid"
    except (errors.EmptyValueError, ValueError, errors.CannotCoerceError, errors.InvalidEmailError, TypeError) as e:
        if isinstance(e, (errors.EmptyValueError, errors.CannotCoerceError, TypeError)):
            sys.exit("You must provide an email address")
        elif isinstance(e, (ValueError, errors.InvalidEmailError)):
            return "Invalid"

    
if __name__ == "__main__":
    main()