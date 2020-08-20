"""
Local Scope:
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""

# Sample 1
a = 100  # global variable

def num1():
    a = 20  # local variable
    print('Value 1 is', a)


def num2():
    a = 50  # local variable
    print('Value 2 is', a)


num1()
num2()

print('-' * 100)

# Sample 2
superUser = 'mike'

def user1(name):
    superUser = name  # local variable. name (argument) as value of superUser variable
    print('Local super user name is', superUser)


superUser = 'bob'  # mike change to bob (new value) as global variable

user1('saddam')
print('Global super user is', superUser)

print('-' * 100)

# Sample 3 (Invalid local scope)
# Type 1
# def num2():
#     a = 'saddam'
#
#
# def main2():
#     print('My name is', a)  # a is part of num2()
#
#
# main2()

# Type 2
# def num3():
#     print('The number is', a)
#     a = 50  # a must before print() (sequential)
#
#
# num3()