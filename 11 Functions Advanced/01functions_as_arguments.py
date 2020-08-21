

# Sample 1
def add1():
    total = 10 + 43
    return total


def sub1():
    total = 10 - 43
    return total


def view2(func1, func2):
    print(f'10 + 43 = {func1()}')
    print(f'10 - 43 = {func2()}')


def main1():
    view2(add1, sub1)


main1()

print('-' * 100)

# Sample 2 (Math operational)
def add2(a, b):
    total = a + b
    return total


def sub2(a, b):
    total = a - b
    return total


def view2(func, a, b):
    print('------ Result ------')
    if func == add2:
        print(f'{a} + {b} = {func(a, b)}')
    else:
        print(f'{a} - {b} = {func(a, b)}')


def main2():
    print('1. Addition')
    print('2. Subtraction')
    math2 = int(input('Type Math Operational That You Want: '))
    print('-' * 10)

    if math2 == 1:
        val1 = int(input('Input value 1: '))
        val2 = int(input('Input value 2: '))

        add2(val1, val2)
        view2(add2, val1, val2)

    elif math2 == 2:
        val1 = int(input('Input value 1: '))
        val2 = int(input('Input value 2: '))

        sub2(val1, val2)
        view2(sub2, val1, val2)

    else:
        return


main2()

print('-' * 100)

# Sample 3
def sq(func, x):  # func = 4, x = 2
    exp = x ** 2  # exp = 4
    return func(exp)  # call f(x)


def f(x):  # x = 4
    return x ** 2  # 2 ** 2 = 4


main3 = sq(f, 2)
print(main3)
