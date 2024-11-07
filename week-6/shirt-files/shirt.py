import sys
from param_check import check_parameter_file
from PIL import Image, ImageOps

def main():
    validate_params()

    im1 = open_shirt()

    im2 = open_selfie()

    if im2.size != (600, 600):
        im2 = ImageOps.fit(im2, (600, 600))
    
    im2.paste(im1, im1)
    
    try:
        im2.save(f"{sys.argv[2]}")
    except OSError as e:
        print("\nError caught at NewImageSave:\n", e)
        sys.exit(f"\nErrror creating new image.\n")
    

def open_shirt():
    try:
        im1 = Image.open("shirt.png")
    except (OSError, TypeError) as e:
        print(f"\nError caught at OpenShirt:\n", e)
        sys.exit(f"\nError opening required file, shirt.png")
    
    return im1

def open_selfie():
    try:
        im2 = Image.open(f"{sys.argv[1]}")
    except (OSError, TypeError) as e:
        print(f"\nError caught at OpenSelfie:\n", e)
        if isinstance(e, TypeError):
            sys.exit(f"\n{sys.argv[1]}: Image type not supported\n")
        else:
            sys.exit(f"\nError opening {sys.argv[1]}")

    return im2


def validate_params():
    error1 = check_parameter_file(2, 3, "png", "PNG")
    error2 = check_parameter_file(2, 3, "jpg", "JPG")
    error3 = check_parameter_file(2, 3, "jpeg", "JPEG")

    if error1 == None or error2 == None or error3 == None:
        pass
    else:
        if error1 != None:
            sys.exit(error1)
        elif error2 != None:
            sys.exit(error2)
        elif error3 != None:
            sys.exit(error3)



if __name__ == "__main__":
    main()