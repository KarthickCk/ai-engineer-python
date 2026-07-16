# 🎯 Day 4 Challenge — Note Saver
# Run:  python3 note_saver.py
#
# Fill in every line marked  # YOUR CODE  then run it a few times.
# Each note should STICK AROUND between runs — that's a real persistent app!


# 1) Ask the user for a note.
note = input("Type your note: ")

# 2) Append the note to my_notes.txt.
#    "a" = append mode: creates the file if missing, adds to the end otherwise.
#    Don't forget the  \n  so each note lands on its own line!
with open("my_notes.txt", "a") as file:
    # YOUR CODE: write  note  followed by "\n"
    file.write(note + "\n")  # YOUR CODE: write note followed by "\n"

# 3) Read the WHOLE file back and print every saved note.
print("\n=== All your saved notes ===")
with open("my_notes.txt", "r") as file:
    # YOUR CODE: read the file into a variable and print it
    notes = file.read()  # YOUR CODE: read the file into a variable
    print(notes)  # YOUR CODE: print the variable
