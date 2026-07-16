# Script 1 — Making decisions with if / elif / else.
# Run it with:  python3 01_if_else.py

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("-" * 30)

# elif = "else if" — check multiple conditions in order:
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

print("-" * 30)

# Comparison operators you can use:
#   ==  equal to        !=  not equal
#   >   greater than    <   less than
#   >=  greater/equal   <=  less/equal

# Combine conditions with  and / or / not :
temperature = 30
is_sunny = True

if temperature > 25 and is_sunny:
    print("Perfect beach day! ☀️")

if temperature > 40 or not is_sunny:
    print("Maybe stay inside.")

print("\n")
print("-" * 30)
print("=== Time of Day ===")
print("-" * 30)

hour = 12

if hour < 12 and hour >=6:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
elif hour < 22:
    print("Good evening!")
else:
    print("Good night!")
# TRY IT: write an if/elif/else that prints a message based on a "hour" variable
#         (morning / afternoon / evening / night).
