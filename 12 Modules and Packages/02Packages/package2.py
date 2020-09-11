# Access Package With __init__.py in arithmetics_operator

# Sample 1: Using import
# import arithmetics_operator
#
# print(arithmetics_operator.addition(10, 2))
# print(arithmetics_operator.subtraction(10, 2))
# print(arithmetics_operator.division(10, 2))
# print(arithmetics_operator.multiplication(10, 2))

# Sample 2: Using from
from arithmetics_operator import addition, subtraction, division, multiplication

print(addition(10, 2))
print(subtraction(10, 2))
print(division(10, 2))
print(multiplication(10, 2))