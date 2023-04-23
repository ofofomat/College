switcher = input('Do you want to convert to Fahrenheit(F) or Celsius(C)?\n')

if switcher == 'F' or 'f':
    farenheit = float(input('What is the temperature in Farenheit? '))
    farenheit = (5*(farenheit-32)/9)
    print('The temperature, in Celsius, currently is: '+str("{:.2f}".format(farenheit)))
elif switcher == 'C' or 'c':
    farenheit = float(input('What is the temperature in Farenheit? '))
    farenheit = (farenheit*1.8)+32
    print('The temperature, in Fahrenheit, currently is: '+str("{:.2f}".format(farenheit)))