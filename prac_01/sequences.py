"""
CP1404/CP5632 - Practical
Menu-driven number sequence generator
"""

MENU = "(E) Show even numbers from X to Y \n(O) Show odd numbers X to Y \n(S) Squares of numbers from X to Y \n(Q) Quit"
start_range = int(input("Enter value 'X': "))
finish_range = int(input("Enter value 'Y': "))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        for i in range(start_range, finish_range):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == "O":
        for i in range(start_range, finish_range):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == "S":
        pass
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell.")

