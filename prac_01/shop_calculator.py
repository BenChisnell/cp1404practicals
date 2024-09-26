# Part A

total = 0
number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price_of_item = float(input("Price of item: "))
    while price_of_item < 0:
        print("Invalid price")
        price_of_item = float(input(f"Price of item: "))
    total = total + price_of_item
if total < 100:
    total = total
else:
    total = total - (total * 0.1)
print(f"Total price for {number_of_items} items is ${total:.2f}")

# Part B

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price_of_item = float(input("Price of item: "))
    while price_of_item < 0:
        print("Invalid price")
        price_of_item = float(input(f"Price of item: "))
    total = total + price_of_item
if total < 100:
    total = total
else:
    total = total - (total * 0.1)
print(f"Total price for {number_of_items} items is ${total:.2f}")
