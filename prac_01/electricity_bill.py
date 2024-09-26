""" CP1404/CP5632 - Practical
Electricity bill estimator
"""

# Part A

print("Electricity bill estimator")
kwh_price = int(input("Enter cents per kWh: "))
daily_usage = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
estimated_bill = kwh_price / 100 * (daily_usage * billing_period)
print(f"Estimated bill: ${estimated_bill:.2f}")



# Electricity bill estimator - Part B

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_usage = float(input("Enter daily use in kWh: "))
billing_period = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = TARIFF_11 * (daily_usage * billing_period)
else:
    estimated_bill = TARIFF_31 * (daily_usage * billing_period)
print(f"Estimated bill: ${estimated_bill:.2f}")