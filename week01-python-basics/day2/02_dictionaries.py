# Script 2 — Dictionaries (labelled data: key -> value).
# Run it with:  python3 02_dictionaries.py

# A list uses positions (0, 1, 2). A dictionary uses NAMES (keys).
# Use curly braces {} with  key: value  pairs.
person = {
    "name": "Karthick",
    "age": 34,
    "goal": "AI engineer",
}

print(person)                # the whole dictionary
print(person["name"])        # look up a value BY ITS KEY -> "Karthick"
print(person["goal"])        # "AI engineer"

# Add or change a value:
person["city"] = "Chennai"   # add a new key
person["age"] = 35           # change an existing one
print(person)

# Safe lookup (won't crash if the key is missing):
print(person.get("email", "no email set"))   # "no email set"

# See all keys / all values:
print(person.keys())
print(person.values())

# WHY THIS MATTERS: AI APIs send and receive data as dictionaries (JSON).
# Every Claude API response you'll use later is basically a dictionary.

# TRY IT: make a dictionary describing a movie (title, year, rating). Print the title.

movie = {
    "title": "King",
    "year": "2023",
    "rating": "5"
}

print(movie["rating"])

movie["rating"] = "4"
print(movie.get("director", "Director not found"))

print(movie.keys())
print(movie.values())
