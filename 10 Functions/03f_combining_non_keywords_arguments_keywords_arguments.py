"""
We can use both non keyword arguments and keyword arguments combined.
"""

# Sample 1
def args(a, *b, **c):
    print('Formal Argument:', a)
    print('-' * 10)
    for i in b:
        print('Non Keyword Argument:', i)
    print('-' * 10)
    for j, k in c.items():
        print('Keyword Argument:', j, '=', k)


args(12, 'satu', 'dua', 'tiga', name = 'saddam', age = 23, address = 'Indonesia')  # 12 = a (positional), 'satu' --> 'tiga' = *b (tuples), name --> address = **c (dictionaries)


# Invalid arguments
# def args(a, **b, *c)  # positional arguments (a) must follows by non keyword arguments (*c) then follows by keyword arguments (**b)
# def args(**a, b, *c)  # first slots given for positional arguments