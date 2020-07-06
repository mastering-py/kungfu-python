# Python has a set of built-in functions and methods that you can use on tuples

# 1. Functions
print('len()')
# To determine how many items a tuple has, use the len() function:
tuple1 = (10, 1, 'dua', 200, 4.5, True, 'Hello World')
print(len(tuple1))
print()

print('max()')
# Return the largest value
# We cannot return the largest values of tuple that contains BOTH string values AND numeric values
tuple2 = (10, 1, 200, 4.5, -2, 0)
print(max(tuple2))
print()

print('min()')
# Return the lowest value
# We cannot return the largest values of tuple that contains BOTH string values AND numeric values
tuple3 = (10, 1, 200, 4.5, -2, 0)
print(min(tuple3))
print()

print('sorted()')
# Sorted tuple
# We cannot sort a tuple that contains BOTH string values AND numeric values
tuple4 = (10, 1, 200, 4.5, -2, 0)
a = sorted(tuple4)
print(a)
print(type(a)) # it converts to list
print()

print('+' * 100)
print()

# #2. Methods
print('count()')
# Return the number of times the value "dua" appears the data1.
data1 = (10, 1, 'dua', 200, 4.5, True, 'dua', 'Hello World', 'dua', 3, 100)
b = data1.count('dua')
print(b)
print()

print('index()')
# Returns the index of the first element with the specified value
data2 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
b = data2.index(4.5)
print(b)