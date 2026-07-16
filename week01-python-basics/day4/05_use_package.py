# Script 5 — Using a package you installed with pip (requests).
# FIRST do the venv steps in 04_venv_and_pip.md and run: pip install requests
# Then run:  python3 05_use_package.py

# 'requests' is not built into Python — you installed it with pip.
# It lets you call APIs over the internet (you'll use this idea for AI APIs too).
import requests

print("Fetching a random piece of advice from an API...")

# Call a free public API (returns JSON):
response = requests.get("https://api.adviceslip.com/advice")

# Turn the JSON response into a Python dictionary:
data = response.json()

# Dig into the data (it looks like: {"slip": {"id": 1, "advice": "..."}}):
advice = data.get("slip", {}).get("advice")

print("-" * 40)
print("💡 Advice of the moment:")
print(advice)
print("-" * 40)

# WHY THIS MATTERS: this is EXACTLY the shape of calling an AI API —
# send a request, get JSON back, dig out the part you want. You just did it!

# TRY IT: run this a few times — you'll get different advice each time.
# If you get an error about 'requests' not found, your venv isn't active
# or you haven't run  pip install requests  yet.
