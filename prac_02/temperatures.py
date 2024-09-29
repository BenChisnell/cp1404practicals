"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
from prac_01.temperatures import fahrenheit

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius_to_fahrenheit(fahrenheit)
            print(f"{fahrenheit:.2f}")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_Fahrenheit_to_Celsius(celsius)
            print(f"{celsius:.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
