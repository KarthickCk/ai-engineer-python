# Script 3 — For loops (do something for each item).
# Run it with:  python3 03_for_loops.py

# Instead of writing print() 4 times, loop over a list:
skills = ["Python", "Git", "JavaScript", "React"]

for skill in skills:
    print("I am learning:", skill)

print("-" * 30)   # prints a line of 30 dashes (neat trick!)

# range() gives you numbers to loop over:
for number in range(1, 6):      # 1, 2, 3, 4, 5  (stops BEFORE 6)
    print(f"Day {number}")

print("-" * 30)

# Loop over a dictionary (get key AND value):
person = {"name": "Karthick", "age": 34, "goal": "AI engineer"}
for key, _ in person.items():
    print(f"{key}: {person.get(key)}")

# TRY IT: loop over your food list from script 1 and print "Yum: <food>" for each.

foods = ["Pizza", "Ice Cream", "Burgers"]

for food in foods:
    print("Yum:", food)
