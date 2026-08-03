seat_type = input("Enter seat type (sleeper/general/AC/luxury): ").lower()

print("-" * 40, "\n")

match seat_type:
    case "sleeper":
        print("Sleeper seat selected. Price: $50")
    case "general":
        print("General seat selected. Price: $30")
    case "ac":
        print("AC seat selected. Price: $70")
    case "luxury":
        print("Luxury seat selected. Price: $100")
    case _:
        print("Invalid seat type. Please choose from sleeper, general, AC, or luxury.")