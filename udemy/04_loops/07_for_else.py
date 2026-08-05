staff = [("Alice", 10), ("Bob", 26), ("Charlie", 25)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is {age} years old.")
        break
else:
    print("No one is 18 or older.")