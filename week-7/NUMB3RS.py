import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}$", ip):
        for split in ip.split(".", 3):
            if int(split) > 255:
                return "False"
            if "0" in split and len(split) > 1:
                return "False"
            
        return "True"
    
    return "False"


if __name__ == "__main__":
    main()