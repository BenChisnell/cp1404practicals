"""CP1404 - Programming II
Get a valid score from a user (Between 0-100 inclusive), print that number and print that number of stars (*).
"""

MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit   "
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        score = int(input("Score: "))
        while score < 0 or score > 100:
            print("Invalid score!")
            score = int(input("Score: "))
    elif choice == "P":
        print(f"Score is: {score}")
        print()
    elif choice == "S":
        for i in range(score):
            print("*", end="")
        print()
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell.")
