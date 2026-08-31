# chai = "Giner tea"

# def prepare_tea(order):
#     print(f"Preparing {order}...")

# prepare_tea(chai)
# print(chai)

# chai = ["Masala tea", "Ginger tea", "Green tea"]

# def edit_chai(cup):
#     chai[0] = cup

# edit_chai("Lemon tea")
# print(chai)

# def make_chai(tea, milk, sugar):
#     print(f"Making {tea} with {milk} and {sugar}")

# make_chai(tea="Masala tea", milk="full cream milk", sugar="2 tsp sugar") # keyword arguments

# def special_chai(*ingredients, **extras):
#     print(f"Making special chai with {ingredients}")
#     print(f"Extras: {extras}")

# special_chai("Masala tea", "Ginger tea", milk="full cream milk", sugar="2 tsp sugar") # keyword arguments

# def chai_orders(order=[]):
#     order.append("Masala tea")
#     print(f"Preparing {order}...")

def chai_orders(order=None):
    if order is None:
        order = []
    order.append("Masala tea")
    print(f"Preparing {order}...")

chai_orders()
chai_orders()