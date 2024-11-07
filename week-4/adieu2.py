import sys
import inflect

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names = get_names(names)
        except (EOFError) as e:
            say_adieu(names)
            break

def get_names(names):
    names.append(input("Name: "))
    
    if "" in names:
        sys.exit("You cannot provide a blank name")
    
    return names

def say_adieu(names):
    line = "Adieu, adieu, to "

    if len(names) == 0:
        print(line + names[0])

    else:
        print(line + p.join(names))
            
if __name__ == "__main__":
    main()