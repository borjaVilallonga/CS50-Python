import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
         print("Too few command-line arguments")
    elif len (sys.argv) > 3:
         print("Too many command-line arguments")

    imput_extension = os.path.splitext(sys.argv[1])[1].lower()
    output_extension = os.path.splitext(sys.argv[2])[1].lower()

    valid_extension = [".jpg", ".jpeg", ".png"]

    if imput_extension not in valid_extension:
         sys.exit("Invalid input")

    if output_extension not in valid_extension:
             sys.exit("Invalid output")

    if imput_extension != output_extension:
          sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, shirt)

    photo.save(sys.argv[2])

main()
