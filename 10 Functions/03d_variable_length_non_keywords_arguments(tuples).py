"""
Variable Length Non keyword arguments (Tuples):
Variable length non keyword arguments are useful when we are not certain about number of arguments that are required in
the function definition or function would receive. Any left over actual (positional) arguments are captured by python
as a tuple, which is available through variable which is having prefixed * in the function definition.
"""

# Sample 1: Single non keyword argument
def args(*a):
    print('Non Keyword Arguments:', a)
    print('-' * 10)
    for i in a:
        print('Non Keyword Argument:', i)


args(1, 2, 3, 4, 'lima', 6, 7)  # the arguments packaged to tuple

print('-' * 100)

# Sample 2: Many non keyword argument
def args(a, b, *c):
    print('Positional Argument:', a)
    print('Positional Argument:', b)
    print('-' * 10)
    for i in c:
        print('Non Keyword Argument:', i)


args(10, 2)
args(b = 'sepuluh', a = 'dua') # we can use keyword only argument for positional arguments, without any non keywords arguments inside the parentheses
args(1, 2, 3, 4, 'lima', 6, 7)  # (*c = 3, 4, 'lima', 6, 7). captured by python as a tuple

# Sample 3: Invalid non keyword arguments
# def args(a, *b, *c)  # two non keywords arguments in parameter are invalid
# def args(*a, b, c)  # first slots given for positional arguments
# def args(a, *b, c)   # positional arguments (a and c) must follow by non keywords arguments (*b)