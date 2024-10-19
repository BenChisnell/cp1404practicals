"""
CP1404 Practical
Quick Picks
"""
import random

MINIMUM = 1
MAXIMUM = 80
NUMBERS_PER_LINE = 10

number_of_quick_picks = 2
# number_of_quick_picks = int(input("How many quick picks? "))
"""Print random number of quick picks from user input"""
for i in range(number_of_quick_picks):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()

    print(" ".join(f"{number:2}" for number in numbers))
