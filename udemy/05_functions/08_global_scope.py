chai_type = "Ginger Chai" # global scope

def front_desk():
    def kitchen():
        global chai_type  # Accessing global scope
        chai_type = "Masala Chai"  # Modifying global scope
        print(f"Inside kitchen: {chai_type}")

    kitchen()

front_desk()
print(f"Outside kitchen: {chai_type}")