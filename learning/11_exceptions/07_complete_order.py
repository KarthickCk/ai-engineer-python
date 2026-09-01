class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger": 30}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} is not available")
        if not isinstance(cups, int):
            raise InvalidChaiError(f"Cups must be integers")
        total = menu[flavor] * cups
        print(f"Your bills for {flavor} {cups} is rupees {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you!")

bill("mint", 2)
bill("masala", "three")
bill("masala", 3)

