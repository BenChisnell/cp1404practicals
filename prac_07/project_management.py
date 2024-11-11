"""
CP1404 Practical
Project Management Program
Estimate: 2.5 hours
Actual:
"""
from datetime import datetime
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
            load_projects(projects)

        elif choice == "S":
            save_project()

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            pass

        elif choice == "A":
            add_new_project(projects)

        elif choice == "U":
            pass

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Would you like to save to projects.txt?")
    print("Thank you for using custom-built project management software.")


def load_projects(projects):


def get_data(filename):
    """Extract data from TXT file and return it as a list"""
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(parts)

    return projects


def add_new_project(projects):
    name = input("Project name: ")
    date = input("Date (DD/MM/YYYY): ")
    priority = int(input("Priority: "))
    estimate = int(input("Cost estimate: "))
    completion = int(input("Completion: "))
    add_to_project = ([name, date, priority, estimate, completion])
    projects.append(add_to_project)


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(project)

    print("Completed projects: ")
    for project in completed_projects:
        print(project)


def save_project():
    name = input("Filename: ")
    with open("name.txt", "w") as out_file:
        print(name, file=out_file)
        out_file.close()


main()
