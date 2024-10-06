# What did you see on line 1?
# The values: 18, 19, 16
# Smallest number: 5
# Largest number: 19
#
# What did you see on line 2?
# The values: 5, 9, 3
# Smallest number: 3
# Largest number: 9
# Line 4 could not produce a "4" as the start is 3, max number is 9 (10 minus 1), and the count increments
# are in 2's'. Produce all odd numbers
#
# What did you see on line 3?
# 3.783753622719789, 4.05045973725259, 4.95687944666601
# Smallest number: 2.5
# Largest number: 5.5
# (random uniform prints random float numbers between a low and high number - inclusive)


import random

random_number = random.randint(1, 100)
print(f"Random number is: {random_number}")
