class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    specialAges = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

    def growOld(self):
        self.age += 1
        if self.age < 21:
            self.growUp(0.5)
        elif self.age in self.specialAges:
            self.growUp(-1)

    def getFat(self, kilos):
        self.weight += kilos

    def getFit(self, kilos):
        self.weight -= kilos

    def growUp(self, cm):
        self.height += cm
