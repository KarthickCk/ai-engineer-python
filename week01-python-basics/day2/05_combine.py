# Script 5 — Putting it together: a list of dictionaries + a loop.
# Run it with:  python3 05_combine.py

# This is one of THE most common patterns in real code (and in AI apps).
# A list, where each item is a dictionary:
students = [
    {"name": "Asha",  "score": 88},
    {"name": "Ravi",  "score": 72},
    {"name": "Meena", "score": 95},
    {"name": "Vikram", "score": 67},
]

# Loop through them and print a report:
print("=== Score Report ===")
for student in students:
    name = student["name"]
    score = student["score"]
    status = "PASS" if score >= 75 else "RETRY"   # inline if/else
    print(f"{name}: {score}  ->  {status}")

# Calculate the average score:
total = 0
for student in students:
    total += student["score"]      # add each score to the total
average = total / len(students)
print(f"\nClass average: {average}")

# WHY THIS MATTERS: when Claude's API returns a list of results,
# this exact pattern is how you'll read through them.

# TRY IT: add a 4th student to the list, then run again. The report updates automatically!
