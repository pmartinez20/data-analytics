# rentals.py
# Calculate van rentals for a tour group

import math

num_tourists = int(input("How many tourists are going on the tour? "))

seats_per_van = 15
cost_per_van = 250

vans_needed = math.ceil(num_tourists / seats_per_van)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / num_tourists

print(f"Number of tourists: {num_tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van rental cost: ${format(total_cost, '.2f')}")
print(f"Cost per person: ${format(cost_per_person, '.2f')}")
