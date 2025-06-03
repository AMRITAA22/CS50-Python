import sys
import random
from pyfiglet import Figlet
def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Invalid font")
    else:
        sys.exit("Usage: figlet.py [-f FONT]")
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))
if __name__ == "__main__":
    main()
