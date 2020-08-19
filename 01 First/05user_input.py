# Python allows for user input using input() function

username = input('Input your username: ')

print(username)
print(type(username)) # the input data type is string

print('-' * 100)

# Math in input
a = int(input('Input number 1: '))
b = int(input('Input number 2: '))
c = a + b
# or
# c = int(a + b)
print(f'{a} + {b} = {c}')

print('-' * 100)

# Other sample
print('Type your name:')
name = input()
print('Type your password:')
pwd = int(input())
print('=' * 10)
print('Your name is', name)
print('Your password is', pwd)