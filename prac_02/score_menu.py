"""CP1404 - Programming II
Get a valid score from a user (Between 0-100 inclusive), print the score and score category, and print that score (number) of stars (*).
"""

MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_results(score)
        elif choice == "S":
            print_character(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """ Get a valid score from a user (Between 0-100 inclusive) """
    score = int(input("Enter a valid score (0-100 inclusive): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter a valid score (0-100 inclusive): "))
    print()
    return score


def determine_users_score(score):
    """Determine the category of a users' valid score"""
    if score < 0 or score > 100:
        category = "Invalid"
    elif score < 50:
        category = "Bad"
    elif score < 90:
        category = "Pass"
    else:
        category = "Excellent"
    return category


def print_results(score):
    """Print the result of a valid score"""
    category = determine_users_score(score)
    print(f"Your score of {score} is {category}")
    print()


def print_character(score):
    """Print number of '*'s for that valid score amount"""
    for i in range(score):
        print("*", end="")
    print()


main()
