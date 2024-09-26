password_length = 4
user_password = input("Enter your password: ")
while len(user_password) < password_length:
    print(f"Password doesn't meet minimum length, which is {password_length} characters.")
    user_password = input("Enter your password: ")

for i in range(len(user_password)):
    print("*", end="")
