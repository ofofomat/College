num1 = int(input('Type a integer number: '))
num2 = int(input('Type another one: '))

for num1 in range(num1, num2):
    num1 += 1
    if num1 == num2:
        break
    print(num1)
