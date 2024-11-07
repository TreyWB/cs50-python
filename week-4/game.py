import random
import sys

def main():
    while True:
        try:
            level = get_level()
        except ValueError:
            pass
        else:
            answer = random.randint(1, level)
            break

    while True:
        try:
            guess(answer)
        except ValueError:
            pass
        else:
            break
    
def get_level():
    level = int(input("Level: "))
    
    if level < 1:
        raise ValueError
    
    return level

def guess(answer):
    guess = int(input("Guess: "))

    if guess < 1:
        raise ValueError
    
    if guess < answer:
        print("Too small!")
        raise ValueError
    elif guess > answer:
        print("Too large!")
        raise ValueError
    else:
        sys.exit("Just right!")

if __name__ == "__main__":
    main()