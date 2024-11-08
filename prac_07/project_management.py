"""
CP1404 Practical
Project Management Program
Estimate: 2.5 hours
Actual:
"""

MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects  \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project\n- (Q)uit"

print("Welcome to Pythonic Project Management")
print("Loaded 5 projects from projects.txt")
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
