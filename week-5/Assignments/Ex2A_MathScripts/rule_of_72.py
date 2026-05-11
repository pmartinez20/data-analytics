# rule_of_72.py
# How long will it take a savings account to double using the Rule of 72?

savings = 5000
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
doubled_balance = savings * 2

print(f"Your current savings is {savings}.")
print(f"At a {format(interest_rate, '.0%')} interest rate, your savings account will be worth {format(doubled_balance, '.2f')} in {format(years_to_double, '.1f')} years")
