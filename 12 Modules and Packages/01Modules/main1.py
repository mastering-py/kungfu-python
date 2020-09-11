# Sample 1: Use a module
# import modul1
#
# print(modul1.addition(10, 2))
# print(modul1.subtraction(10, 2))

# Sample 2: Use a module by renaming or create an alias
# import modul1 as m1
#
# print(m1.addition(10, 2))
# print(m1.subtraction(10, 2))

# Sample 3: Import specific names (attributes) from a module
# a. Use a modul with one attribute
# from modul1 import addition
#
# print(addition(10, 2))

# b. Using a modul with many attributes
# from modul1 import addition, subtraction
#
# print(addition(10, 2))
# print(subtraction(10, 2))

# c. Using a modul with all attributes
from modul1 import *

print(title)
print(addition(10, 2))
print(subtraction(10, 2))
#
# """
# Sample 3c note:
# # It is recommended to not to use import * because it ignore the risk of namespace collisions.
# # Namespace is a concept of names (identifier) mapping in an object.
# """
