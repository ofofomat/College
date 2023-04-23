user = input('What is your user? ')
password = input('What is your password? ')

if user == password:
    while True:
        print('Error, user and password cannot be the same!')
        password = input('Type your password: ')
        if user != password:
            break

confirmPassword = input('Confirm your password: ')

if password != confirmPassword:
    while True:
        print('Error, passwords do not match!')
        confirmPassword = input('Confirm your password: ')
        if password == confirmPassword:
            break
