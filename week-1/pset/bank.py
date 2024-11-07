import sys

def main():
    user_input = input("Greeting: ")
    user_input = user_input.lower()

    winnings(user_input)

def winnings(raw):
    correct_greeting = "hello"

    if correct_greeting in raw:
        print("$0")
        sys.exit()
    elif raw[0] == correct_greeting[0]:
        print("$20")
        sys.exit()
    else: print("$100")

main()