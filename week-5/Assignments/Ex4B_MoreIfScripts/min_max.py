# min_max.py
# Display the smallest and largest of three numbers

a = 42
b = 17
c = 89

# Find minimum
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find maximum
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
