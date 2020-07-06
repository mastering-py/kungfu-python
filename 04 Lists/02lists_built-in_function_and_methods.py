# Python has a set of built-in functions and methods that you can use on lists

# 1. Functions
print('len()')
# To determine how many items a list has, use the len() function:
list1 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
print(len(list1))
print()

print('max()')
# Return the largest value
# We cannot return the largest values of list that contains BOTH string values AND numeric values
list2 = [10, 1, 200, 4.5, -2, 0]
print(max(list2))
print()

print('min()')
# Return the lowest value
# We cannot return the lowest values of list that contains BOTH string values AND numeric values
list3 = [10, 1, 200, 4.5, -2, 0]
print(min(list3))
print()

print('sorted()')
# Sorted list
# We cannot sort a list that contains BOTH string values AND numeric values
list4 = [10, 1, 200, 4.5, -2, 0]
print(sorted(list4))
print()

print('+' * 100)
print()

#2. Methods
print('insert()')
# Inserts the specified value at the specified position.
data1 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data1.insert(7, 'saddam')
print(data1)
print()

print('append()')
# Adds an element at the end of the list
data2 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data2.append(10000)
print(data2)
print()

print('extend()')
# Add the elements of a list (or any iterable), to the end of the current list
data3 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
x = [1, 2, 'saddam', 'xyz']
data3.extend(x)
print(data3)
data3.extend('abc') # iterable
print(data3)
print()

print('remove()')
# Removes the item with the specified value
data4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data4.remove('Hello World')
print(data4)
print()

print('pop()')
# Removes the element at the specified position
data5 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data5.pop(-2)
print(data5)
print()

print('reverse()')
# Reverses the order of the list
data6 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data6.reverse()
print(data6)
print()

print('index()')
# Returns the index of the first element with the specified value
data7 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
y = data7.index('dua')
print(y)
print()

print('sort()')
# Sorts the list
# We cannot sort a list that contains BOTH string values AND numeric values
data8 = ['saddam', 'rahmat', 'fuad', 'fitri']
data8.sort()
print(data8)
print()

print('clear()')
# Removes all or empties the elements from the list
data9 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
data9.clear()
print(data9)
print()

print('copy()')
# Returns a copy of the list
data10 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
a = data10.copy() # a will not be a reference to data10
a[0] = 'sepuluh'
print(data10)
print(a)
print()

print('count()')
# Return the number of times the value "dua" appears the data11 list. Same as list reference
data11 = [10, 1, 'dua', 200, 4.5, True, 'dua', 'Hello World', 'dua', 3, 100]
b = data11.count('dua')
print(b)


