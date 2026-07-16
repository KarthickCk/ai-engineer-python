# Script 5 — Getting input from the user (interactive!).
# Run it with:  python3 05_input.py

# name = input("What is your name? ")
# goal = input("What do you want to become? ")

# print(f"Nice to meet you, {name}!")
# print(f"Your goal: become a {goal}. You've got this. 🚀")

# # NOTE: input() always gives you a string. To do math on it, convert:
# age = input("How old are you? ")
# age_number = int(age)            # turn the text "25" into the number 25
# print(f"In 5 years you'll be {age_number + 5}.")

# # TRY IT: ask the user for two numbers and print their sum.

balance = input("What is your current bank balance? ")
spend = input("how much you spend? ")

remaminig = float(balance) - float(spend)
print(f"{remaminig} is your remaining balance")
