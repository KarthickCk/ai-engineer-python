essential_spices = {"cardomom", "ginger"}
optional_spices = {"ginger", "cloves"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only essential: {only_in_essential}")

print(f"cloves is in optional: {'cloves' in optional_spices}")