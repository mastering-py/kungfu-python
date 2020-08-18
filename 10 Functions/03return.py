# To let a function return a value, use the return statement

# Sample 1
def main():
    print('Hello world')

    # Type 1: we can let a value without variable
    return 'saddam'

    # Type 2: return a value using variable
    # name = 'saddam 2'
    # return name


# main()  # default calling a function. the return value will not view
# print(main())  # calling a function with print() function will view the 'hello world' stings with the return value
a = main()
print(a)  # assign a function to a variable will view the 'hello world' stings with the return value

print('-' * 100)

# Sample 2 (Simple numeric return value)
def val1():
    total = 12 + 3
    return total


print(val1())  # View the return value using print()
a = val1()
print(a)  # by assign to the variables

print('-' * 100)

# Sample 3 (Difference between View the return value using print() function and by assign to the variables method)
def val1():
    print('Input 1 ')
    value1 = int(input('Input value: '))
    return value1


def val2():
    print('Input 2 ')
    value2 = int(input('Input value: '))
    return value2

# View the return value using print()
# print(f'{val1()} + {val2()} = {val1() + val2()}')  # with this calling method, the input of val1() and val2() functions will becomes twice with invalid numeric operations

# View the return value by assign to the variables
a = val1()
b = val2()
print(f'{a} + {b} = {a + b}')  # using assign to the variables, it will only take the return value

print('-' * 100)

# Sample 4 (Return list value and combine with for loop)
def items():
    list1 = ['satu', 'dua', 'tiga', 'empat']
    return list1


def main():
    for i in items():
        print(i)


main()

print('-' * 100)

# Sample 5 (Return tuple value)
def Tampilkan():
    return 1, 2, 3, 'wadi', 3, 2, 1  # we can let the return value using tuple


print(Tampilkan())
print(type(Tampilkan()))

