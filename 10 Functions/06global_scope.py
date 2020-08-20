"""
Global scope:
A variable created outside of a function is global and can be used by anyone (global and local)
"""

# Sample 1
a = 100  # global variable

def user1():
    print('User 1 score is', a)


def user2():
    print('User 2 score is', a)


print('Score:')
user1()
user2()

print('\nNew score:')
a = 69  # new global variable value

user1()
user2()

print('-' * 100)

# Sample 2 (Global keyword)
# The global keyword makes the variable global
name = 'andy'
age = 21

def user3(a, b):
    global name, age  # the local variables change to global
    name = a
    age = b

    print('Name:', name)
    print('Age:', age)


user3('mat', 30)
print(f'Current global data are: \nName: {name}, Age: {age}')