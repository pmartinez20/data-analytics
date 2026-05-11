# address_entry.py

contact_info = {
    "name": "Paola",
    "address": "123 Michigan Ave",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
}

# Print formatted mailing address
print(f"""{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

# --- Remove name key ---
del contact_info["name"]

# --- Add full_name as a nested dictionary ---
full_name = {
    "first name": "Paola",
    "last name": "Johnson"
}

# --- Add honorific using .update() ---
full_name.update({"honorific": "Ms."})

# --- Add full_name to contact_info using .update() ---
contact_info.update({"full_name": full_name})

# --- Print formatted address with new items ---
print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")
