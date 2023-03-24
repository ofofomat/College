class Square:
    def __init__(self, side):
        self.side = side

    def sideSize(self, value):
        self.side = value

    def printSide(self):
        print(f'{self.side}')

    def calcArea(self):
        return self.side*self.side


square = Square(3)

square.sideSize(2.5)
square.printSide()
print(square.calcArea())
