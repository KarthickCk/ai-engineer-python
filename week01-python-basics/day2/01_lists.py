# Script 1 — Lists (an ordered collection of items).
# Run it with:  python3 01_lists.py

# A list holds many values in one variable. Use square brackets [].
skills = ["Python", "Git", "JavaScript"]

print(skills)              # the whole list
print(skills[0])           # "Python"  (first item — counting starts at 0!)
print(skills[-1])          # "JavaScript"  (last item)
print(len(skills))         # 3  (how many items)

# Add and remove items:
skills.append("React")     # add to the end
print(skills)              # now has 4 items

skills.remove("Git")       # remove a specific item
print(skills)

# Change an item:
skills[0] = "Python 3.14"
print(skills)

# Check if something is in the list:
print("React" in skills)   # True

# TRY IT: make a list of 3 foods you like, add a 4th, then print the list.

foods = ["Pizza", "Sushi", "Ice Cream"]
foods.append("Burgers")
print(foods)

foods.remove("Sushi")
print(foods)

drinks = []
drinks.append("Water")
print("Water" in drinks)
