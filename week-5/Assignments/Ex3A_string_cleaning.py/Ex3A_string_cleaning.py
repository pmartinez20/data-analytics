# Ex3A_string_cleaning.py
# Clean up messy contact records

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# --- Convert names to lowercase ---
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# --- Convert names to title case ---
print(name_1.title())
print(name_2.title())
print(name_3.title())

# --- Remove $ from salary strings ---
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")
print(salary_1_clean)
print(salary_2_clean)
print(type(salary_1_clean))  # still a string! need to remove comma and cast to int for math

# --- Chain .replace() and int() to produce usable integer from salary_1 ---
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)
print(type(salary_1_int))
