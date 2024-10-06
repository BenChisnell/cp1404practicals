# Q1.

out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()


 # Q2.
in_file = open("name.txt")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


 # Q3.
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

 # Q4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)