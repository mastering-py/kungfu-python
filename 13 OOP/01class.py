# Almost everything in Python is an object, with its attributes and methods.
# To create a class, use the keyword class.

# Sample 1: Create a class without any attributes
class Heroes1:
    pass


print(Heroes1())  # The output is memory address of Heroes class

print('-' * 100)

# Sample 2: Create a class with its attributes
# Type 1: Attributes outside of the class
class Heroes2:
    pass


# Attributes:
Heroes2.name = 'Superman'
Heroes2.power = 100
Heroes2.health = 100

# Access the class variables
print(Heroes2.name)
print(Heroes2.power)
print(Heroes2.health)

print()

# Type 2: Attributes inside of the class
class Heroes3:
    # Attributes for Heroes3 class (Class Variables)
    name = 'Superman'
    power = 100
    health = 100


# Access the class variables
print(Heroes3.name)
print(Heroes3.power)
print(Heroes3.health)
