# complex_taxes.py
# Calculate federal tax based on annual gross income and filing status

pay_rate = float(input("Enter hourly pay rate: $"))
hours_worked = float(input("Enter hours worked this week: "))
filing_status = input("Enter filing status ('single' or 'joint'): ").strip().lower()

# Calculate weekly gross pay (with overtime)
if hours_worked <= 40:
    weekly_gross = pay_rate * hours_worked
else:
    regular_pay = pay_rate * 40
    overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
    weekly_gross = regular_pay + overtime_pay

# Estimate annual gross pay
annual_gross = weekly_gross * 52

# Determine tax rate based on filing status and income
if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print("Invalid filing status. Please enter 'single' or 'joint'.")
    tax_rate = 0

weekly_tax = weekly_gross * tax_rate
net_pay = weekly_gross - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${format(pay_rate, '.2f')} per hour, your gross weekly pay is ${format(weekly_gross, '.2f')}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${format(weekly_tax, '.2f')}")
print(f"Your net pay is ${format(net_pay, '.2f')}")
