def main():
    orig = input("What do you want to convert? ")
    print("Converted:",convert(orig))
    
def convert(string):
    edited = string.replace(":)", "🙂").replace(":(", "🙁")
    return edited

main()