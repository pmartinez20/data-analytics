# candy_store.py

# Two tuples: candy types and fruity flavors
candy_types = ("gummy bears", "hard candy", "lollipops", "jellybeans")
fruity_flavors = ("strawberry", "watermelon", "mango", "peach")

# Create a set of candy combinations
candy_combinations = set()
candy_combinations.add(candy_types[0] + " - " + fruity_flavors[1])   # gummy bears - watermelon
candy_combinations.add(candy_types[1] + " - " + fruity_flavors[0])   # hard candy - strawberry
candy_combinations.add(candy_types[2] + " - " + fruity_flavors[3])   # lollipops - peach
candy_combinations.add(candy_types[3] + " - " + fruity_flavors[2])   # jellybeans - mango

print("Today's candy options include:")
print(candy_combinations)
print("Today's candy options include:")
print(candy_combinations)
print("Today's candy options include:")
print(candy_combinations)
# Notice: the order of items in a set changes each time you print it!
# Sets are unordered - Python does not guarantee any particular order
