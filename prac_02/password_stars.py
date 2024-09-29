""" Ask the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable."""


def main():
    password_length = 4
    user_password = get_password(password_length)
    print_password_as_astericks(user_password)


def print_password_as_astericks(user_password):
    """Print password values into '*'s' """
    for i in range(len(user_password)):
        print("*", end="")


def get_password(password_length):
    """Compares user password length against a password length variable"""
    user_password = input("Enter your password: ")
    while len(user_password) < password_length:
        print(f"Password doesn't meet minimum length, which is {password_length} characters.")
        user_password = input("Enter your password: ")
    return user_password


main()
