import sys
import pyfiglet
import random
    
# Validate that user provided correct flags and parameters
def validate_flags():
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")
    
    fonts = pyfiglet.FigletFont.getFonts()
    
    # Validate user provided a figlet-supported font
    if sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")

# Get random figlet-supported font, to use in main()
def get_random_font():
    fonts = pyfiglet.FigletFont.getFonts()
    font = random.choice(fonts)
    
    return font

# Check how many parameters user provided
if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 3:
    validate_flags()
else:
    sys.exit("Invalid Usage")


def main():
    original = input("Input: ")
    
    random = get_random_font()
    
    # Convert user input string to Figlet
    # Check if user provided a desired font
    if len(sys.argv) == 3:
        converted = pyfiglet.figlet_format(f"{original}",font=f"{sys.argv[2]}")
    # If user didn't provide a font, we use a random font
    else:
        converted = pyfiglet.figlet_format(f"{original}",font=f"{random}")

    print(f"Output:\n{converted}", end="")



if __name__ == "__main__":
    main()