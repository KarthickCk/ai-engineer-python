# 🎯 Week 1 Finale — CLI To-Do List
# Run:  python3 todo.py
#
# Fill in every  # YOUR CODE  spot. Build & test ONE function at a time.
# Everything you need you already learned in Days 1-4.

TASKS_FILE = "tasks.txt"


# --- Load tasks from the file into a list (so they persist between runs) ---
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())   # .strip() removes the trailing \n
    except FileNotFoundError:
        print("No file found")   # No file yet on the very first run — that's fine, start empty.
    return tasks


# --- Save the current list back to the file (one task per line) ---
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:      # "w" = rewrite the whole file
        for task in tasks:
            file.write(task)
            file.write("\n")

# --- Add a task to the list ---
def add_task(tasks):
    task = input("New task: ")
    save_tasks(task)
    print(f"Added: {task}")


# --- Show all tasks, numbered 1, 2, 3... ---
def list_tasks(tasks):
    if len(tasks) == 0:
        print("(no tasks yet)")
        return
    print("--- Your tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


# --- Remove a task by its number ---
def remove_task(tasks):
    list_tasks(tasks)
    if len(tasks) == 0:
        return
    number = int(input("Remove which number? "))   # convert text -> int
    # A number like 1 is at index 0, so subtract 1. Check it's in range first.
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)   # .pop(index) removes & returns that item
        print(f"Removed: {removed}")
    else:
        print("That number doesn't exist.")


# --- The main menu loop ---
def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO ===")
        print("1) Add   2) List   3) Remove   4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Bye! 👋")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


# This line runs main() when you execute the file.
main()
