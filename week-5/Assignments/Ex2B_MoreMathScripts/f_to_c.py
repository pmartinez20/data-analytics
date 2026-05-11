# f_to_c.py
# Convert a temperature from Fahrenheit to Celsius

fahrenheit = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {celsius:.2f}°C")
