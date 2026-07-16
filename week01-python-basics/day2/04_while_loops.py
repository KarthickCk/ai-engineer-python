# Script 4 — While loops (repeat WHILE a condition is true).
# Run it with:  python3 04_while_loops.py

# A for-loop runs a fixed number of times.
# A while-loop runs until something changes. Careful: it can run forever!

count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1        # IMPORTANT: change the value, or it loops forever!

print("Done counting.")
print("-" * 30)

# Countdown example:
seconds = 3
while seconds > 0:
    print(f"{seconds}...")
    seconds -= 1             # shortcut for  seconds = seconds - 1
print("Blast off! 🚀")

# TRY IT: use a while loop to print the numbers 10 down to 1.

number = 10
while number > 0:
    print(number)
    number -= 1
