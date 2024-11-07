def main():
    tries = question()
    
    if tries >= 3:
        print("Incorrect")
    else:
        print("Correct")

def question():
    tries = 1
    while tries <= 3:
        answer = int(input("3 + 3 = "))
        
        if answer == (3 + 3):
            return tries
        else:
            tries += 1
    
    return tries



main()