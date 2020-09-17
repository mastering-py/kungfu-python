teacher = 'saddam'

def school():
    # global headmaster  # to test headmaster read as global
    headmaster = 'maria'
    teacher = 'james'

    print('Inside school(), my teacher is', teacher)
    print('dir() inside school():\n', dir())  # to returns all properties and methods of local scope without the values
    print('vars() inside school():\n',vars())  # to returns all properties and methods of local scope with keys and values in dictionary


print('Outside school(), my teacher is', teacher)
print('dir() outside school():\n', dir())  # to returns all properties and methods of global scope without the values
print('dir() outside school():\n', vars())  # to returns all properties and methods of global scope with keys and values in dictionary

print()
school()

# print()
# print('to test headmaster read as global')
# print('Outside school(), my headmaster is', headmaster)  # this statement must after school() function
# print('dir() outside school():\n', dir())
# print('dir() outside school():\n', vars())
