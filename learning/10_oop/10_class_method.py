class ChaiOrder:

    def __init__(self, type_, sweetness, size):
        self.type = type_
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dictionary(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(
            tea_type,
            sweetness,
            size
        )

class ChaiUtils:

    @staticmethod
    def isValidSize(size):
        return size in ["small", "Large", "medium"]


print(ChaiUtils.isValidSize("Medium"))

order1 = ChaiOrder.from_dictionary({"tea_type": "masala", "sweetness":"medium", "size": "small"})
order2 = ChaiOrder.from_string("Ginger,masala,small")
order3 = ChaiOrder("Large", "medium", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)