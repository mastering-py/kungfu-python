# Yes/No condition using while loop
choice = 'y'  # this condition is true

while choice == 'y':
    name = input('What is your name?: ')
    age = int(input('How old are you?: '))

    print('======== Your Data ========')
    print(f'Your name is {name}')
    print(f'You are {age} years old')

    choice = input('Want to repeat (y/n)?: ')  # the while loop will stop except 'y' key

print('-' * 100)
