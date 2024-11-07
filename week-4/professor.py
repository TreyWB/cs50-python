import random

def main():
    # Initialize variables for get_problem()
    fails = 0
    incorrect = 0

    while True:
        try:
            level = get_level()
        except ValueError:
            pass
        else:
            break

    for i in range(10):
        fails = get_problem(fails, level, incorrect)
        
        i += 1

    # Display score
    score = 10 - fails
    print(f"Score: {score}")


def get_level():
    level = int(input("Level: "))
    
    if not 1 <= level <= 3:
        raise ValueError
    
    return level


def generate_integer(level):
    if level == 1:
        random_int = random.randint(0, 9)
    elif level == 2:
        random_int = random.randint(10, 99)
    elif level == 3:
        random_int = random.randint(100, 999)
        
    return random_int


def get_problem(fails, level, incorrect):
    int1 = generate_integer(level)
    int2 = generate_integer(level)
    
    answer = int1 + int2
   
    while True:
        try:
            user_guess = int(input(f"{int1} + {int2} = "))
            if user_guess != answer:
                raise ValueError

        except ValueError:
            incorrect += 1
            print("EEE")
            
            if incorrect == 3:
                print(f"{int1} + {int2} = {answer}")
                fails += 1
                return fails

        else:
            return fails



if __name__ == "__main__":
    main()