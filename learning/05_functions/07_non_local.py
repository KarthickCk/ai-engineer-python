def update_order():
    chai_type = "Masala Chai"  # local scope

    def kitchen():
        nonlocal chai_type  # Accessing enclosing scope
        chai_type = "Ginger Chai"  # Modifying enclosing scope
        print(f"Inside kitchen: {chai_type}")

    kitchen()
    print(f"Outside kitchen: {chai_type}")

update_order()