
name = input("What's your name? ")

if len(name) < 3:
    while True:
        print('Your name must be at least 3 charecters long!')
        name = input('Type your name again: ')
        if len(name) >= 3:
            break

age = float(input("What's your age? "))

if age < 0 or age > 150:
    while True:
        print('That is NOT your real age. Is it?!')
        age = float(input('Type your true age, please: '))
        if age > 0 or age < 150:
            print('Thanks for being honest with yourself')
            break

wage = float(input("What's your wage? "))

if wage < 0:
    while True:
        print('That is NOT a valid wage amount')
        wage = float(input('Type your wage: '))
        if wage > 0:
            break

acceptGenders = ['f', 'm']
gender = (input("What's your gender? ")).lower()

if gender not in acceptGenders:
    while True:
        print('That is NOT a valid gender for this form')
        gender = input('Type your BIRTHgender: ').lower()
        if gender in acceptGenders:
            break
