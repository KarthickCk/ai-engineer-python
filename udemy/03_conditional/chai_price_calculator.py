cup_size = input("What size cup would you like? (small, medium, large) ").lower()

prices = {"medium": 3, "large": 5, "small": 1}

if cup_size in prices:
    price = prices[cup_size]
    print(f"The price for a {cup_size} cup of chai is ${price}.")
else:
    print(f"Sorry, we do not have a price for a {cup_size} cup of chai.")