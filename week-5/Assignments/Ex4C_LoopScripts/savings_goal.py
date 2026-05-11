# savings_goal.py

bank_balance = 500
savings_goal = 2000
weekly_savings = 150

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal:
        break
    elif bank_balance >= savings_goal * 0.75:
        treat = 10
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}")
    elif bank_balance >= savings_goal * 0.50:
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}")
    else:
        print(f"This week my balance increased to ${bank_balance:.2f}")

print(f"Goal met! My current balance is ${bank_balance:.2f}")
