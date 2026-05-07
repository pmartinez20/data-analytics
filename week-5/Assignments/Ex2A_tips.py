#Formula: Total Due is determined by: Food Cost + Tax + Tip
#Script:
# Define known values

food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
print("The total due is " + str(total_due))
#97.
#Str is used because you cant combine a string and a number in python. so str converts the float into text 
#print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#food cost is 79.25 and tax is 6.54
print("Tip is " + str(tip))
#tip is 12.0
print("Total due is " + str(total_due))
#Total due is 97.79
print("Tip is " + format(tip, ".2f"))
#12.00

