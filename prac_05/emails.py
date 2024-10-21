"""
CP1404 Practical
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Estimate: 40 minutes
Actual: 1 hour, 15min
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        correct_name = input(f"Is your name {name}? [Y/n]").upper()
        if correct_name != "Y" and correct_name != "":
            name = input("Name: ")
        name_to_email[email] = name
        email = input("Email: ")

    for email, name in name_to_email.items():
            print(f" {name} ({email})")


def extract_name(email):
    """Extract name from email address entered by the user."""
    text = email.split('@')[0]
    parts = text.split('.')
    name = " ".join(parts).title()
    return name


main()
