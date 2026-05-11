# tiles.py
# Calculate how many boxes of tiles to buy for a room

length = float(input("Enter room length (ft): "))
width = float(input("Enter room width (ft): "))

tiles_per_box = 12
tile_size = 1  # 1ft x 1ft

area = length * width
tiles_needed = area  # each tile is 1 sq ft

# Add 10% extra for chips, breakage, mess-ups
tiles_with_buffer = tiles_needed * 1.10

import math
boxes_needed = math.ceil(tiles_with_buffer / tiles_per_box)

print(f"Room area: {area} sq ft")
print(f"Tiles needed (with 10% buffer): {math.ceil(tiles_with_buffer)}")
print(f"Boxes to buy: {boxes_needed}")
