# Script 1 — Writing to files.
# Run it with:  python3 01_write_files.py

# "w" = write mode (creates the file, or overwrites if it exists).
# The  with  keyword safely opens and auto-closes the file for you.
with open("notes.txt", "w") as file:
    file.write("My first line written by Python.\n")   # \n = new line
    file.write("Second line.\n")
    file.write("Third line.\n")

print("Wrote to notes.txt — check the file in this folder!")

print("-" * 30)

# "a" = append mode (adds to the end, keeps existing content).
with open("notes.txt", "a") as file:
    file.write("This line was appended later.\n")

print("Appended one more line.")

# TRY IT: write a file  goals.txt  with 3 of your learning goals, one per line.

with open("goals.txt", "w") as file:
    file.write("Learn Python basics.\n")
    file.write("Build a small project.\n")
    file.write("Contribute to open source.\n")
