character = input('Type any letter: ')

checker = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

if character in checker:
    print('Vowal')
else:
    print('Consonant')
