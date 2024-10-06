# Q1.
#
# name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()
from ast import literal_eval

# Q2.
# in_file = open("name.txt")
# text = in_file.read()
# in_file.close()
# print(f"Hi {text}!")
# NOT WORKING

# Q3.
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        value = int(in_file.readline())
        print(value)
    in_file.close()

# with open("numbers.txt", "r") as in_file:
#     in_file
#     print(in_file)
# in_file.close()

# with open("numbers.txt", "r") as in_file:
#     text = in_file.read()
#     in_file.close()
#     print(text)