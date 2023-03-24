class Rectangle:
    def __init__(self, aSide, bSide):
        self.aSide = aSide
        self.bSide = bSide

    def changeSideValues(self, newA, newB):
        self.aSide = newA
        self.bSide = newB

    def printSides(self):
        print(f'a side is {self.aSide} while b side is {self.bSide}')

    def calcArea(self):
        return self.aSide*self.bSide

    def calcPer(self):
        return (self.aSide*2)+(self.bSide*2)


floor = Rectangle(0, 0)

floor.aSide = float(input('Type the value of one side of the floor: '))
floor.bSide = float(input('Type the value of the other side of the floor: '))

tread = 0.5

qntTreads = floor.calcArea()

footer = floor.calcPer()

print(f'The area is: {floor.calcArea()}')
print(f'The amount of treads will be: {qntTreads/tread}')
print(f'While the size (in meters) of footer needed is: {footer}')
