aCountry = float(input('People in country A: '))
bCountry = float(input('People in country B: '))

if bCountry < aCountry:
    trader = bCountry
    bCountry = aCountry
    aCountry = bCountry

aRate = float(input('Birth rate in country A: '))
bRate = float(input('Birth rate in country B: '))

i = 1
while True:
    if aRate < bRate:
        print('The less populate country will never reach the more populated one!')
        break
    aCountry = aCountry+(aCountry*aRate)*i
    bCountry = bCountry+(bCountry*bRate)*i
    if aCountry > bCountry:
        print("{:.0f}".format(aCountry))
        print(' | ')
        print("{:.0f}".format(bCountry))
        print(f'in the {str(i)}th year')
        break
    else:
        i += 1
