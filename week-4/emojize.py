import emoji

def main():
    original = input("Input: ")
    
    converted = emoji.emojize(original, language='alias')
    
    print(f"Output: {converted}")



if __name__ == "__main__":
    main()