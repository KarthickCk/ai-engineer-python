class Chaicup:
    size = 150

    def describe(self):
        return f"A {self.size}ml chai cup"

simple_cup = Chaicup()
print(Chaicup.describe(simple_cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))
