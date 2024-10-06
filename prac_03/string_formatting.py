"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# TODO: Use f-string formatting to produce the output:
print(f"{year} {name} for about ${cost:.0f}!")


number = 2
power_of = 0
for i in range(power_of, 11):
    print(f"{number} ^ {i:>2} is {number ** i:>4}")