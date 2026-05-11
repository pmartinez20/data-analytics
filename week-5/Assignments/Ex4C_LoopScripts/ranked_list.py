# ranked_list.py

favorites = ["Chicago", "Tokyo", "Cartagena", "Paris", "Nairobi", "Mexico City"]

# Print numbered list starting at 1
for index, item in enumerate(favorites, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")

# BONUS: print in reverse order, still numbered 1 through len
print("\nReversed:")
for index, item in enumerate(reversed(favorites), start=1):
    print(f"{index}. {item}")
