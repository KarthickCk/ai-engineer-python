# favourite_chai = [
#     "Masala chai",
#     "Green tea",
#     "Lemon tea",
#     "Giner tea",
#     "Masala chai",
#     "Green tea"
# ]

# unique_chai = {chai for chai in favourite_chai if len(chai) > 10}
# print(unique_chai)

receipes = {
    "Masala chai": ["ginger", "cardomon", "clove"],
    "Elaichi chai": ["milk", "cardomon"],
    "Spicy chai": ["ginger", "clove", "black peppre"]
}

unique_spices = {spice for menu in receipes.values() for spice in menu}
print(unique_spices)

