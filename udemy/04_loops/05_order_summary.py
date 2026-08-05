names = ["Alice", "Bob", "Charlie"]
bills = [25.50, 30.75, 15.00]

for item in zip(names, bills):
    name, bill = item
    print(f"{name} owes ${bill:.2f}")