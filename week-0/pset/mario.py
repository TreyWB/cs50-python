def main():
    height = int(input("Height: "))
    
    print()
    for i in range(height):
        print(" " * (height - i), "#" * (i + 1))
    

main()