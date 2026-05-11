# Description: This script tests various numeric
# conversion techniques
# Author: Paola

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# --- Cast as integer using int() ---
# int(a)   # ValueError: invalid literal - can't convert a string with spaces/decimals directly
int(b)     # works: 55
# int(c)   # ValueError: invalid literal - contains non-numeric characters
# int(d)   # ValueError: invalid literal - contains non-numeric characters

# --- Cast as float using float() ---
float(a)   # works: 101.1 (Python strips whitespace)
float(b)   # works: 55.0
# float(c) # ValueError: invalid literal - contains non-numeric characters
# float(d) # ValueError: invalid literal - contains non-numeric characters

# --- For variable a: cast into float then integer ---
int(float(a))  # works: 101 (strips spaces, converts to float first, then truncates decimal)

# --- Slicing to extract numeric portion and cast ---
a_num = int(float(a.strip()))   # strip spaces, convert to float, then int -> 101
c_num = int(c[:3])              # slice first 3 chars "402", cast to int -> 402
d_num = int(d.strip()[-1])      # slice last character "5", cast to int -> 5

# --- Print value and type of each original variable ---
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# --- Use .strip() to remove leading/trailing spaces ---
print(a.strip())  # "101.1"
print(d.strip())  # "Number 5"
