masala_spices = ( "cinnamon", "cardamom", "cloves")

(spice1, spice2, spice3) = masala_spices

print(f"Spice 1: {spice1}, Spice 2: {spice2}, Spice 3: {spice3}")

cinamon_ratio, cardamom_ratio = (0.5, 0.3)
print(f"Cinnamon ratio: {cinamon_ratio}, Cardamom ratio: {cardamom_ratio}")

cinamon_ratio, cardamom_ratio = cardamom_ratio, cinamon_ratio
print(f"Cinnamon ratio: {cinamon_ratio}, Cardamom ratio: {cardamom_ratio}")

print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")
