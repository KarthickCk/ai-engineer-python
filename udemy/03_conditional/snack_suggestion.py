entered_snack = input("What snack would you like? ").lower()

if entered_snack == "cookies" or entered_snack == "samosa":
    print(f"Great! choice! You can have {entered_snack}.")
else:
    print(f"Sorry! {entered_snack} is not available. we only serve cookies and samosa.")