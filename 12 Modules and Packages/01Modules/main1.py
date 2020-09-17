# Sample 1: Access a module
# import modul1
#
# print(modul1.addition(10, 2))
# print(modul1.subtraction(10, 2))

# Sample 2: Access a module by renaming or create an aliases
# import modul1 as m1
#
# print(m1.addition(10, 2))
# print(m1.subtraction(10, 2))

# Sample 3: Access specific names (attributes) from a module
# a. Using a module with one attribute
# from modul1 import addition
#
# print(addition(10, 2))

# b. Using a module with multiple attributes
# from modul1 import addition, subtraction
#
# print(addition(10, 2))
# print(subtraction(10, 2))

# c. Using a module with all attributes
# from modul1 import *
#
# print(title)
# print(addition(10, 2))
# print(subtraction(10, 2))
#
# """
# Sample 3c note:
# # It is recommended to not to use import * because it ignore the risk of namespace collisions.
# # Namespace is a concept of names (identifier) mapping in an object.
# """

# d. Using aliases in from access
from modul1 import addition as add, subtraction as sub

print(add(10, 2))
print(sub(10, 2))
