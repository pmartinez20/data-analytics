# movie_list.py

movie_list = [
    "The Devil Wears Prada",
    "Clueless",
    "Inception",
    "Parasite",
    "Spirited Away",
    "Get Out",
    "Everything Everywhere All at Once"
]

print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)

# --- Print sorted list two ways ---

# Using sorted() - does NOT modify the original list
print(sorted(movie_list))
print(movie_list)
# Notice: sorted() returns a new sorted list but movie_list is unchanged

# Using .sort() - modifies the original list in place
movie_list.sort()
print(movie_list)
# Notice: .sort() permanently changes the order of movie_list

# --- Add a new movie with .append() ---
movie_list.append("Whiplash")
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)
