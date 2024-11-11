import csv
from operator import itemgetter

from prac_07.guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitars.append(parts)

    in_file.close()

    guitars.sort(key=itemgetter(1), reverse=True)
    print(f"{guitars}")


main()
