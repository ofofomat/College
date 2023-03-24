num1 = float(input('Type a number: '))
num2 = float(input('Type another one: '))
if num1 > num2:
    print(str("{:.3f}".format(num1)+' is the higher number'))
elif num2 > num1:
    print(str("{:.3f}".format(num2)+' is the higher number'))
else:
    print("They're the same!")