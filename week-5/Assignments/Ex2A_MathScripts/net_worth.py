#1. How do you calculate your net worth given your assets and debts?
#a) Start by brainstorming: What are “assets” that would need to be included in this
#calculation? What about “debts”?
#b) Discuss and figure out the formula and what the script would look like, making up
#example values as needed.
#c) Now create the script in a file named net_worth.py
#d) Your displayed output should be formulated as follows (3 print statements):
#Your total assets are [number]

#Assets 
savings = 1500
car = 25000

#Debts 
taxes_due = 5000
credit_card = 4100

total_assets = savings + car 
total_debts = taxes_due + credit_card 
net_worth = total_assets - total_debts 

print("total assets are", total_assets)
#26500
print("Your total debts are", total_debts)
#9100
print("Your net worth is", net_worth)
#17400

#2. How do you calculate the area of a rectangle?
#a) Say you have a rectangle that has dimensions corresponding to your birthday – the
#month number is one side and the day of the month is the other side. How would
#you calculate the area of this rectangle?
side_a = 7 
side_b = 24
area = 7 * 24 
#b) Figure out the formula and what the script would look like, and create the script in a
#file named area_of_rectangle.py
#c) The displayed output should be formatted as follows:
#Side A is [number]
#Side B is [number]
#The area of the rectangle is [number]
print(area)
#d) Once your script is working, save and commit your changes.

#3. How do you calculate the tip amount on a restaurant bill given the tip percentage?
#a) Figure out the formula and what the script would look like, making up example
#values as needed. (If you need inspiration, what was your approximate restaurant
#bill the last time you ate at a restaurant?)

#b) Create the script in a file named tip_amount.py
#c) The displayed output should be formatted as follows:
#The tip on a $[number] restaurant bill is $[number]
#d) Once your script is working, save and commit your changes.
#4. How do you calculate the area of a circle?
#a) The diameter of a given circle is the same as the day of your birthday (not the month,
#just the day). Figure out the formula, refresh your recollection of the difference
#between diameter and radius, and figure out what the script should look like.
#b) Create the script in a file named area_of_circle.py
#c) The displayed output should be formatted as follows:
#The area of a circle with radius [number] is [number]
#Year Up United Data Analyst Training Academy Week 5 Lab Workbook
#Page 21 of 43
#d) Once your script is working, save and commit your changes.
#5. How long will it take a savings account worth X to double in value based on an interest
#rate of IR? (Hint: Look up the “rule of 72”)
#a) Figure out the formula and what the script would look like, making up example
#values as needed.
#b) Create the script in a file named rule_of_72.py
#c) The displayed output should be formatted as follows:
#Your current savings is [number].
#At a [number]% interest rate, your savings account will be
#worth [number] in [number] years
#d) Show your doubled balance with 2 digits to the right of the decimal point by using
#format(__, ".2f") and show years with 1 digit to the right of the decimal. How
#can you do this using format()?
#e) There are a couple ways you might get the interest rate to display as a percentage.
#One option is to use the format function. In this case, instead of including the
#character f to assign a fixed decimal format, use the character % to assign the
#percentage format, e.g. format(__, ".0%")
#f) When you get the script working, commit your changes