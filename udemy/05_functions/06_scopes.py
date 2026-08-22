def serve_chai():
    chai_type = "Masala Chai" # local scope
    print(f"Inside function {chai_type}")

chai_type = "Ginger Chai" # global scope
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order = "lemon" # Enclosing scope

    def print_chai_order():
        chai_order = "ginger" # local scope
        print(f"Inner: {chai_order}") # Accessing enclosing scope
        
    print_chai_order()
    print(f"Outer: {chai_order}") # Accessing enclosing scope

chai_order = "masala" # global scope
chai_counter()
print(f"Global: {chai_order}") # Accessing global scope