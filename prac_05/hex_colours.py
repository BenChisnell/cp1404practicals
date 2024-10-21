"""
CP1404 Practical
Create a program that allows you to look up hexadecimal colour codes
"""

COLOUR_CODES = {"absolute zero": "#0048ba", "alizarin crimson": "#e32636", "amethyst": "#9966cc", "aqua": "#00ffff",
                "army green": "#4b5320",
                "aureolin": "#fdee00", "baby blue": "#89cff0", "barn red": "#7c0a02", "black": "#000000",
                "blueviolet": "#8a2be2"}

print(COLOUR_CODES)
colour_name = input("Colour name: ").lower()
while colour_name != "":
    print(f"The colour code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Colour name: ").lower()
