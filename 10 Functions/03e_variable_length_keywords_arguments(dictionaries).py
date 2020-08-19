"""
Variable length keyword arguments (Dictionaries):
Python captures all extra keyword arguments as dictionary and makes it available by name(variable) which is prefixed
by ** in the function definition.
"""

# Sample 1: Single keyword argument
def args(**a):
    print('Keyword Arguments:', a)
    print('-' * 10)
    for i, j in a.items():  # dictionary iterable
        print('Keyword Argument:', i, '=', j)


args(Name = 'saddam', age = 23, address = 'Indonesia')  # the arguments packaged to dictionaries

print('-' * 100)

# Sample 2: Many keywords arguments
def args(a, b, **c):
    print('Positional Arguments:', a)
    print('Positional Arguments:', b)
    print('-' * 10)
    for i, j in c.items():  # dictionary iterable
        print('Non Keyword Argument:', i, '=', j)


args(12, 'satu', name = 'saddam', age = 23, address = 'Indonesia')  # (a = 12, b = 'satu', **c = Name -> address). positional arguments must follow by keywords arguments and called with the correct position.
print('\nPositional arguments sets by keyword:')
args(a = 12, name = 'saddam', age = 23, address = 'Indonesia', b = 'satu')  # (a and b are positional arguments). when all positional arguments set by keywords, their position doesn’t matter

# Sample 3: Invalid keyword arguments
# def args(a, **b, **c)  # two keywords arguments in parameter are invalid
# def args(**a, b, c)  # first slots given for positional arguments.
# def args(a, **b, c)  # positional arguments (a and c) should follow by keyword arguments (**b)