def main():
    greeting = input("Greeting: ")
    
    greeting = greeting.lower()
    
    if greeting == "hello":
        print("\n$0")
    elif greeting[0] == "h":
        print("\n$20")
    else:
        print("\n$100")