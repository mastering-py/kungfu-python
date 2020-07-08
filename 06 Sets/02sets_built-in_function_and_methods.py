# Python has a set of built-in functions and methods that we can use on sets

# 1. Functions
print('To determine how many items a set has, use the len() function:')
set1 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'} # True == 1
print(len(set1))
print()

print('To return the largest value use max() function:')
# We cannot return the largest values of set that contains BOTH string values AND numeric values
set2 = {10, 1, 200, 4.5, -2, 0}
print(max(set2))
print()

print('To return the lowest value use min() function:')
# We cannot return the lowest values of set that contains BOTH string values AND numeric values
set3 = {10, 1, 200, 4.5, -2, 0}
print(min(set3))
print()

print('To sorted the set use sorted() function:')
# We cannot sort a set that contains BOTH string values AND numeric values
set4 = {10, 1, 200, 4.5, -2, 0}
print(sorted(set4))
print()

print('+' * 100)
print()

#2. Methods
print('Adds an item to the set use add() method:')
data1 = {10, 'dua', 200, 4.5, True, 'Hello World'}
data1.add('tiga')
print(data1)
print()

print('Returns a copy of the set copy() method:')
data2 = {10, 'dua', 200, 4.5, True, 'Hello World'}
# a = data2 # without copy() method, changes made in a, will automatically be made in data2
a = data2.copy()
a.add('sepuluh')
print(data2)
print(a)
print()

print('Returns a set containing the difference between two or more sets use difference() method:')
data3 = {1, 'saddam', 'rahmat', 'fuad'}
data4 = {'saddam', 'fuad', 'fitri', 'along'}
b = data3.difference(data4) # set items in data3 but not in data4
c = data4.difference(data3) # set item in data4 but not in data3
print(b)
print(c)
print()

print('Remove use clear(), discard(), remove() and pop methods:')
# clear()
data5 = {10, 'dua', 200, 4.5, True, 'Hello World'} # removes all the items from the set
data5.clear()
print(data5)
# discard()
data6 = {1, 'saddam', 'rahmat', 'fuad'}
data6.discard(1) # remove the specified item
print(data6)
# remove()
data6.remove('saddam')
print(data6)
# pop()
data6.pop() # Remove the first item from the unindexed set. It will always change between 'rahmat' and 'fuad'
print(data6)
print()

print('Returns a set, that is the intersection of two other sets use intersection() method:')
data7 = {1, 'saddam', 'rahmat', 'fuad', 'along'}
data8 = {'saddam', 'fuad', 'fitri', 'along'}
data9 = {1, 2, 'along'}
d = data7.intersection(data8, data9)
print(d)
print()

print('Join two other sets use union() and update() methods:')
# union()
data10 = {1, 'saddam', 'rahmat', 'fuad', 'along'}
data11 = {'saddam', 'fuad', 'fitri', 'along'}
data12 = {1, 2, 'along'}
e = data10.union(data11, data12)
print(e)
print(len(e))
# update()
data10.update(data11, data12)
print(data10)
data10.update([3, 4, 5]) # join many items using list
print(data10)
