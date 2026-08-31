chai_order = dict(type = "Masala Chai", size = "Large", sugar = 2)
print(f"Chai order: {chai_order}")

print("-" * 20, "\n")

chai_receipe = {}
chai_receipe["base"] = "black tea"
chai_receipe["liquid"] = "milk"
print(f"Chai receipe base: {chai_receipe['base']}")

print("-" * 20, "\n")

del chai_receipe["liquid"]
print(f"Chai receipe after deleting liquid: {chai_receipe}")

print(f"Is sugar in chai_order? {'sugar' in chai_order}")

print("-" * 20, "\n")

chai_order = {"type": "Masala Chai",  "sugar": 1, "size": "Medium"}
print(f"Chai order: {list(chai_order.keys())}")
print(f"Chai order values: {list(chai_order.values())}")
print(f"Chai order items: {list(chai_order.items())}")

print("-" * 20, "\n")

extra_spices = {"cardamom": 2, "cinnamon": 1, "cloves": 3}
chai_order.update(extra_spices)
print(f"Chai order after adding extra spices: {chai_order}")

chai_note = chai_order.get("note", "No special instructions")
print(f"Chai note: {chai_note}")