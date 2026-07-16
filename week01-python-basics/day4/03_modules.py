# Script 3 — Importing modules (using code others wrote).
# Run it with:  python3 03_modules.py

# Python comes with many built-in modules. Use  import  to load them.

import random          # for random numbers/choices
import datetime        # for dates and times
import json            # for working with JSON (VERY important for AI APIs)
import math            # for math functions/constants

# --- random ---
print("Random number 1-100:", random.randint(1, 100))
print("Random skill:", random.choice(["Python", "React", "RAG", "Docker"]))

print("-" * 30)

# --- datetime ---
now = datetime.datetime.now()
print("Right now:", now)
print("Just the year:", now.year)

print("-" * 30)

# --- json --- (this is how AI APIs send/receive data!)
person = {"name": "Karthick", "skills": ["Python", "AI"], "level": 1}

# Turn a Python dictionary INTO a JSON string:
json_text = json.dumps(person, indent=2)
print("As JSON text:")
print(json_text)

# Turn a JSON string BACK into a Python dictionary:
back_to_dict = json.loads(json_text)
print("Name from parsed JSON:", back_to_dict["name"])

print("-" * 30)

print("Math constants/functions:")
print("Square root of 144:", math.sqrt(144))
print("value of pie:", math.pi)
# WHY THIS MATTERS: every Claude API call sends JSON and gets JSON back.
# json.dumps (dict -> text) and json.loads (text -> dict) are your everyday tools.

# TRY IT: import the  math  module and print  math.sqrt(144)  and  math.pi .
