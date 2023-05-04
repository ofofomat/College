class Ball:
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def changeColor(self, newColor):
        self.color = newColor

    def printColor(self):
        print(f'{self.color}')


futBALL = Ball('green', 3.14, 'pvc')

print(futBALL.color)

futBALL.changeColor('red')

futBALL.printColor()
print(futBALL.circumference)

print(futBALL.material)
