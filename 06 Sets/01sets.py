# A set is a collection which is unordered and unindexed, so we cannot be sure in which order the items will appear. In Python sets are written with curly brackets.

# 1. Create set
mySet1 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
print(mySet1)
print(type(mySet1))
print()

# 2. Access items
# We cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# mySet2 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
# print(mySet2[0])
# print()

# 3. Change items value
# Since sets are unordered the items has no index, we can't change its items.
# mySet3 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
# mySet3[5] = False
# print()

# 4. Add items
# To add on item to set, we can use the add() and update() method
# The new items are also not be sure in which order will appear
# The set has removed the duplicates and returned only one of each duplicate items
# add()
mySet4 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'} # True == 1
mySet4.add('tambah')
print(mySet4)
# update()
mySet5 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
mySet5.update(['kurang', 4.5, False])
print(mySet5) # False == 0
print()

# 5. Remove items
mySet7 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
mySet7.remove(200)
print(mySet7)
mySet8 = {10, 1, 'dua', 200, 4.5, True, 'Hello World'}
# We can't remove the set items. But we can delete the set completely
del mySet8
# print(mySet8) this will cause an error because we have succsesfully deleted "mySet8"
print()







