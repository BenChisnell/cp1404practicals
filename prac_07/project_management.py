"""
CP1404 Practical
Project Management Program
Estimate: 2.5 hours
Actual:
"""

from operator import itemgetter

MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects  \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = get_data(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass

        elif choice == "S":
            pass

        elif choice == "D":
            pass

        elif choice == "F":
            pass

        elif choice == "A":
            pass

        elif choice == "U":
            pass

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Would you like to save to projects.txt?")
    print("Thank you for using custom-built project management software.")


def get_data(filename):
    """Extract data from TXT file and return it as a list"""
    projects = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            projects.append(parts)
            # projects.sort(key=itemgetter(1))

    return projects


main()
