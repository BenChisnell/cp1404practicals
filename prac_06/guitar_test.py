"""CP1404 - Week 6 Practical - Guitars"""

from prac_06.guitar import Guitar


def main():
    """Guitar program."""

    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    different = Guitar("Another Guitar", 1997, 45678.75)

    print(f"{guitar.name} get_age() - expected (100). Got {guitar.get_age()}")
    print(f"{different.name} get_age() - expected (25). Got {different.get_age()}")
    print(f"{guitar.name} is_vintage() - expected (True). Got {guitar.is_vintage()} ")
    print(f"{different.name} is_vintage() - expected (False). Got {different.is_vintage()} ")



main()