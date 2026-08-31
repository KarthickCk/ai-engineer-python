# value = 13
# remainder = value % 5

# if remainder:
#     print(f"{value} is not divisible by 5, remainder is {remainder}")

value = 13
if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")

available_size = ["S", "M", "L"]

if (size := input("What size do you want? ")) in available_size:
    print(f"{size} is available.")
else:
    print(f"{size} is not available.")

flavors = ["chocolate", "vanilla", "strawberry"]

print("Available flavors:", flavors)

while (flavor := input("What flavor do you want? ")) not in flavors:
    print(f"{flavor} is not available.")
print(f"{flavor} you chose.")
