ingredients = ["water", "milk", "tea"]
ingredients.append("sugar")

ingredients.remove("milk")

spice_options = ["cinnamon", "cardamom", "cloves"]
chai_ingredients = ["water", "milk", "tea"]
chai_ingredients.extend(spice_options)
chai_ingredients.append("black tea")

last_added = chai_ingredients.pop()
chai_ingredients.sort()

sugar_levels = [1, 3, 5, 8]

base_liquid = ["water", "milk", "beer"]
extra_flavour = ["giner"]

full_liquid_mix = base_liquid * 3

raw_spice = bytearray(b"cinnamon")
raw_spice = raw_spice.replace(b"cinna", b"card")
print(raw_spice)