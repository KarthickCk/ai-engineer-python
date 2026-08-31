class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type}....")

class MasalaChai(BaseChai):

    def add_spices(self):
        print(f"Adding cardomon, ginger. cloved")

class Chaishop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(Chaishop):

    chai_cls = MasalaChai

shop  = Chaishop()

fancy = FancyChaiShop()
fancy.chai.add_spices()
fancy.chai.prepare()