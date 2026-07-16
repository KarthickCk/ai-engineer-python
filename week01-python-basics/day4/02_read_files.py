# Script 2 — Reading from files.
# Run it with:  python3 02_read_files.py
# (Run 01_write_files.py FIRST so notes.txt exists.)

# "r" = read mode (the default).
# Read the WHOLE file as one string:
with open("notes.txt", "r") as file:
    content = file.read()

print("=== Whole file ===")
print(content)

print("=== Line by line ===")
# Loop over the file to read one line at a time:
with open("notes.txt", "r") as file:
    for line in file:
        # .strip() removes the invisible newline at the end of each line
        print("LINE:", line.strip())

print("-" * 30)

# Count the lines:
with open("notes.txt", "r") as file:
    lines = file.readlines()   # gives a LIST, one item per line
print(f"The file has {len(lines)} lines.")
print("The last line is:", lines[-1])

# TRY IT: read your goals.txt file and print each goal with a number in front
#         (1. goal one, 2. goal two, ...). Hint: use  enumerate(lines, 1).

with open("goals.txt", "r") as file:
    goals = file.readlines()

for i, goal in enumerate(goals, 1):
    print(f"{i}. {goal.strip()}")
