# Script 2 — Functions (reusable blocks of code).
# Run it with:  python3 02_functions.py

# A function is a named recipe. Define it once, use it many times.
# Use  def  to define, then call it by its name with ().

def greet():
    print("Hello! Welcome.")

greet()   # call it

print("-" * 30)

# Functions can take INPUTS (called parameters):
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Karthick")
greet_person("Asha")

print("-" * 30)

# Functions can give back a RESULT with  return :
def add(a, b):
    return a + b

result = add(5, 3)      # result is now 8
print("5 + 3 =", result)
print("10 + 20 =", add(10, 20))

# WHY THIS MATTERS: soon you'll write a function like  ask_claude(question)
# and call it whenever you need an AI answer. Functions are the building blocks.

# TRY IT: write a function  multiply(a, b)  that returns a * b. Test it.

def multiply(a, b):
    return a * b

print("2 * 4 =", multiply(2, 4))  # Test the multiply function
