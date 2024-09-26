"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    category = "Invalid"
elif score < 50:
    category = "Bad"
elif score < 90:
    category = "Pass"
else:
    category = "Excellent"
print(f"Your score is {score}, which is {category}")



