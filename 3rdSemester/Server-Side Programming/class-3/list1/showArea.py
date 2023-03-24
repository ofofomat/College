import math

radius = float(input('Type any circle radius: '))

radius = math.pi*(math.pow(radius, 2))

print('The area of this circle is: '+str("{:.2f}".format(radius)))