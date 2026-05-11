# pay_rules.py
# Calculate gross pay with overtime at 1.5x for hours over 40

pay_rate = float(input("Enter hourly pay rate: $"))
hours_worked = float(input("Enter hours worked this week: "))

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

print(f"Pay rate: ${format(pay_rate, '.2f')}/hr")
print(f"Hours worked: {hours_worked}")
print(f"Gross pay: ${format(gross_pay, '.2f')}")
