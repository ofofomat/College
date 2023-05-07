class SquareMaker:
    def __init__(self, side=0):
        self.side = side

    def setSide(self, value):
        self.side = value

    def getSide(self):
        return self.side

    def calcArea(self):
        return self.side*self.side
