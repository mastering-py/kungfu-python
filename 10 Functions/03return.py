# To let a function return a value, use the return statement

# Sample 1
def main():
    # return 'Hello saddam'
    name = 'Hello saddam'
    return name


# print(main())
a = main()  # assign to a variable
print(a)

print('-' * 100)

# Sample 2
def val1():
    value1 = int(input('Input value 1: '))
    return value1


def val2():
    value2 = int(input('Input value 2: '))
    return value2


a = val1()
b = val2()
print(f'{a} + {b} = {a + b}')

print('-' * 100)

# Sample 3
def items():
    list1 = ['satu', 'dua', 'tiga', 'empat']
    return list1


def main():
    for i in items():
        print(i)


main()
