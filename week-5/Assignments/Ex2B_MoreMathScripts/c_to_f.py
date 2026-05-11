# c_to_f.py
# Convert a temperature from Celsius to Fahrenheit

celsius = input("Enter temperature in Celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is {fahrenheit:.2f}°F")
