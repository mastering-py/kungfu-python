# Python allows for user input using input() function

username = input('Input your username: ')

print(username)
print(type(username)) # the input data type is string

# Math in input
a = int(input('Input number 1: '))
b = int(input('Input number 2: '))
c = a + b
# or
# c = int(a + b)
print(f'{a} + {b} = {c}')