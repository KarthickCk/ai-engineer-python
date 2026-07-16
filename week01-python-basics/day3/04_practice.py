# Script 4 — Putting functions + logic + loops together.
# Run it with:  python3 04_practice.py

# A small program that grades a list of students using a function.

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
    
def is_top_student(score):
    return score >= 90

students = [
    {"name": "Asha",  "score": 92},
    {"name": "Ravi",  "score": 68},
    {"name": "Meena", "score": 55},
    {"name": "Vikram", "score": 40},
]

print("=== Report Card ===")
for student in students:
    grade = get_grade(student["score"])
    print(f"{student['name']}: {student['score']} -> Grade {grade}")

# Count how many passed (grade is not F):
pass_count = 0
for student in students:
    if get_grade(student["score"]) != "F":
        pass_count += 1

print(f"\n{pass_count} out of {len(students)} students passed.")

# TRY IT: add a function  is_top_student(score)  that returns True if score >= 90,
#         then print the names of all top students.

print("\n")
print("Top Students:")
for student in students:
    if is_top_student(student["score"]):
        print(f"{student['name']} is a top student!")
