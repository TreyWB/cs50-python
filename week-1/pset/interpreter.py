import sys

def main():
    # Sanitize input
    problem = sanitize(input("Expression: "))

    x = float(problem[0])
    y = (problem[1])
    z = float(problem[2])

    # Error if trying to divide by 0
    if y == "/" and z == 0:
        print("Operation is not supported")
        sys.exit()

    error = False
    answer = math(x, y, z, error)

    answer = float(answer)

    if error == True:
        print("Operation is not supported")
    else:
        print(f"{answer:.1f}")

def sanitize(problem):
    # Split into x,y,z on space
    problem = problem.split(" ")
   
    # Remove entries containing the letter 'a' in-place
    problem = [item for item in problem if item.strip() != ""]

    return problem
   

def math(x, y, z, error):
    answer = 0
    match y:
        case "+":
            answer = x + z
            return answer
        case "-":
            answer = x - z
            return answer
        case "*":
            answer = x * z
            return answer
        case "/":
            answer = x / z
            return answer
        # Error if y != + - * or /
        case _:
            error = True
            return error

main()