import sys
import os
from PIL import Image, ImageOps
def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output must be .jpg, .jpeg, or .png")
    if input_ext != output_ext:
        sys.exit("Input and output must have the same extension")
    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(output_file)
if __name__ == "__main__":
    main()
