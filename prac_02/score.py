"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
def main():

    score = float(input("Enter score: "))
    category = determine_users_score(score)
    print(f"Your score is {score}, which is {category}")
    random_score = random.randint(0, 100)
    print(f"Your random score is: {random_score}, which is {determine_users_score(random_score)}")

def determine_users_score(score):
    if score < 0 or score > 100:
        category = "Invalid"
    elif score < 50:
        category = "Bad"
    elif score < 90:
        category = "Pass"
    else:
        category = "Excellent"
    return category


main()

