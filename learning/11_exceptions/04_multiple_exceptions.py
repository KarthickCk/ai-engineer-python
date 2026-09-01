def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * int(quantity)
        print(f"Total cost is {cost}")
    except KeyError as e:
        print(f"Sorry that chai is not in menu {e}")
    except ValueError as e:
        print(f"Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")