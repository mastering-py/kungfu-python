# Python has a set of built-in functions and methods that we can use on dictionaries

# 1. Functions
print('To determine how many items a dictionary has, use the len() function:')
dict1 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print(len(dict1))
print()

print('To return the largest value use max() function:')
# We cannot return the largest values of dictionary that contains BOTH string values AND numeric values
dict2 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print(max(dict2))
dict3 = {
    1: 'son',
    2: 'wife',
    3: 'father',
    4: 'mother'
}
print(max(dict3))
print()

print('To return the lowest value use min() function:')
# We cannot return the largest values of dictionary that contains BOTH string values AND numeric values
dict4 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print(min(dict2))
dict5 = {
    1: 'son',
    2: 'wife',
    3: 'father',
    4: 'mother'
}
print(min(dict3))
print()

print('To sorted the dictionary by its key, use sorted() function:')
# We cannot sort a dictionary that contains BOTH string values AND numeric values
dict6 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print(sorted(dict6))
print()

print('+' * 100)
print()

# #2. Methods
print('Remove using clear(), pop() and popitem() methods:')
print('clear() is using to removes all the items from the dictionary')
data1 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data1.clear()
print(data1)

print('pop() is using to removes the element with the specified key')
data2 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data2.pop('anak')
print(data2)

print('popitem() is using to removes the last inserted key-value pair')
data3 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data3.popitem()
print(data3)
print()

print('Returns a copy of the dictionary using copy() methods:')
data4 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
a = data4.copy()
# a = data4
a['anak'] = 'lanang'
print(a)
print(data4)
print()

print('Return a list with all dictionary keys with values using items() methods:')
data5 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
b = data5.items()
print(b)
print()

print('Return a list with all dictionary keys using keys() methods:')
data6 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
c = data6.keys()
print(c)
print()

print('Return a list with all dictionary values using values() methods:')
data7 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
d = data7.values()
print(d)
print()

print('Access items using get() methods:')
data8 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
e = data8.get('anak')
print(e)
print(data8.get('ibu'))
print()

print('Returns the value of the specified key using setdefault() methods:')
data9 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data9.setdefault('kakek', 'grandpa')
print(data9)
print()

print('Updates the dictionary with the specified key-value pairs using update() methods:')
data10 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data11 = {
    'paman': 'uncle',
    'bibi': 'auntie'
}
data10.update({'kakek': 'grandpa', 'nenek': 'grandma'})
print(data10)
data11.update(data10)
print(data11)
