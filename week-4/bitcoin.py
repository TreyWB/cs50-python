import sys
import requests

def main():
    try:
        n = float(sys.argv[1])
        if n <= 0:
            raise TypeError
    except (IndexError, TypeError, ValueError) as e:
        if isinstance(e, TypeError):
            sys.exit("Number must be greater than 0")
        elif isinstance(e, ValueError):
            sys.exit("Command-line argument is not a number")
        else:
            sys.exit("Missing command-line argument")

    else:
        price, timestamp = get_price()

    total_price = round(price * n, 2)

    print(f"${total_price:,.2f} as of {timestamp}")
    
def get_price():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if r.status_code != 200:
            raise ValueError

    except (requests.exceptions.JSONDecodeError, requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.InvalidJSONError, ValueError) as e:
        sys.exit("Cannot get price")

    else:
        json_response = r.json()
        
    price = json_response["bpi"]["USD"]["rate_float"]
    
    timestamp = json_response["time"]["updated"]
    
    return price, timestamp



if __name__ == "__main__":
    main()