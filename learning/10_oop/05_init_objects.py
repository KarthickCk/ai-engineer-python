class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of type {self.type}"

order = ChaiOrder(type_="Masala chai", size=200)
print(order.summary())

order_two = ChaiOrder(type_="Giner chai", size=100)
print(order_two.summary())