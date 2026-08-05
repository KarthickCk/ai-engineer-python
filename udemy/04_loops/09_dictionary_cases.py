users = [
    {"id": 1, "total": 100, "coupon":"A"}, 
    {"id": 2, "total": 200, "coupon":"B"}, 
    {"id": 3, "total": 300, "coupon":"C"}
]

discounts = {
    "A": (0.2, 0),
    "B": (0.5, 0),
    "C": (0.0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"User {user['id']} has a discount of {discount}.")
