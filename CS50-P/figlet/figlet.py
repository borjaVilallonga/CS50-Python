import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    fuente = random.choice(figlet.getFonts())
    figlet.setFont(font=fuente)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    figlet.setFont(font = sys.argv[2])

else:
    sys.exit("Invalid usage")

texto = input("Input: ")
print(figlet.renderText(texto))
