# 🎯 Day 3 Challenge — Tip Calculator
# Run it with:  python3 tip_calculator.py
#
# Fill in every line marked  # YOUR CODE  then run it.


# 1) Function that returns the tip amount.
#    Hint: tip = bill * percent / 100
def calculate_tip(bill, percent):
    tip = bill * percent / 100
    return tip


# 2) Function that returns bill + tip.
def calculate_total(bill, tip):
    return bill + tip


# 3) Ask the user for the numbers.
#    input() always gives text, so we wrap it in float() to get a number.
bill = float(input("Enter the bill amount: $"))
percent = float(input("Enter the tip percent: "))

# 4) Use your functions.
tip = calculate_tip(bill, percent)      # calls function #1
total = calculate_total(bill, tip)      # calls function #2

# 5) Print the results, formatted to 2 decimals.
#    The :.2f inside {} means "show 2 digits after the decimal point".
print(f"\nTip:   ${tip:.2f}")
print(f"Total: ${total:.2f}")

# Bonus: if the bill is over 1000, print a message.
# YOUR CODE: an if statement that prints "Big spender! 💰"
if bill > 1000:
    print("Big spender! 💰")
