# Script 4 — Strings (working with text).
# Run it with:  python3 04_strings.py

first = "AI"
second = "engineer"

print(first + " " + second)      # join strings: "AI engineer"
print(first.upper())             # "AI"  -> "AI"
print(second.upper())            # "ENGINEER"
print(second.capitalize())       # "Engineer"
print(len(second))               # 8  (number of characters)
print(second[0])                 # "e"  (first character)
print(second[-1])                # "r"  (last character)
print("engine" in second)        # True (is "engine" inside the word?)

first = first.capitalize()
print("gin" in second)                 # True (is "gn" inside the word?)

# TRY IT: make a variable with your full name and print it in UPPERCASE.
