"""
CP1404 - Programming II
Unreliable  cars
"""

from unreliable_car import UnreliableCar


def main():
    """Test unreliable car"""

    good_car = UnreliableCar("Good", 100, 90)
    dodgy_car = UnreliableCar("Dodgy", 100, 5)

    for i in range(1, 6):
        print(f"Attempt to drive {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i):2}km")
        print(f"{dodgy_car.name} drove {dodgy_car.drive(i):2}km")

    print(good_car)
    print(dodgy_car)


main()
