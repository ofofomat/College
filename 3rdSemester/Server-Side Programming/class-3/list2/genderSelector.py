gender = input('Are you male (M) or female (F)? ')

print(gender)

if gender == 'M' or gender =='m':
    print('Male selected')
elif gender == 'F' or gender =='f':
    print('Female selected')
else:
    print('Are you even a human?')