class Chai:
    origin = "India"

Chai.is_hot = True

# creating objects from Chai

simple_chai = Chai()
print(f"Simple chai: {simple_chai.origin}")

simple_chai.is_hot = False

print(f"Simple chai: {simple_chai.is_hot}")
print(f"Chai: {Chai.is_hot}")

simple_chai.flavor = "Masala"

print(f"Simple Chai: {simple_chai.flavor}")