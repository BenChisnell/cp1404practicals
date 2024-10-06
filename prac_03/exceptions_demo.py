"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
if either the numerator or the denominator has data entered as a float.

2. When will a ZeroDivisionError occur?
When you try and divide the numerator with a denominator value of zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes.

"""

try:
    numerator = int(input("Enter the numerator: "))
    while numerator == 0:
        print("Invalid numerator")
        numerator = int(input("Enter the numerator: "))

    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")