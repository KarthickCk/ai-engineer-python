# Script 3 — Function extras: default values & multiple inputs.
# Run it with:  python3 03_function_details.py

# DEFAULT VALUES: give a parameter a fallback if the caller doesn't provide one.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Karthick")                 # uses default -> "Hello, Karthick!"
greet("Asha", "Good morning")     # overrides    -> "Good morning, Asha!"

print("-" * 30)

# A function that makes a decision and returns a value:
def check_pass(score):
    if score >= 75:
        return "PASS"
    else:
        return "RETRY"

print("Score 80:", check_pass(80))
print("Score 60:", check_pass(60))

print("-" * 30)

# Functions working together — one calls another:
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def format_money(amount):
    return f"${amount:.2f}"        # :.2f = 2 decimal places

cart = [2.50, 3.00, 1.25]
total = calculate_total(cart)
print("Total:", format_money(total))

# TRY IT: write a function  is_even(number)  that returns True if the number
#         is even (hint: use  number % 2 == 0 ). Test it with 4 and 7.

def is_even(number):
    return number % 2 == 0

number = 5.456

print(f"{number:.2f} is even: {is_even(number)}")  # Test with 2
