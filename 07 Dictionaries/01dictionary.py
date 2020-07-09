# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.


# 1. Create dictionary
dict1 = {
    'anak': 'son',  # 'anak' == keys       |       'son' == values
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print(dict1)
print(type(dict1))
print()

# 2. Access items
# We can access the items of a dictionary by referring to its key name, by inside square brackets
dict2 = {
    'one': 'son',
    100: 'wife',
    'ayah': True,
    False: 2.2,
    4.0: ['saddam', 1.5, 'rahmat']
}
print(dict2['one'])
print(dict2[100])
print(dict2['ayah'])
print(dict2[False])
print(dict2[4.0])
print(dict2)
print()

# 3. Change items values
dict3 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
dict3['anak'] = 'lanang'
dict3['istri'] = 'bojo'
dict3['ayah'] = 'bapa'
dict3['ibu'] = 'emma'
print(dict3)

# 4. Add items (keys and values)
dict4 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
dict4['paman'] = 'uncle'
dict4['bibi'] = 'auntie'
print(dict4)
print()

# 5. Remove items
dict5 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
del dict5['anak']
print(dict5)
# del dict5 # this will cause an error because we have succsesfully deleted "dict5"
# print(dict5)
print()

# 6. Operator in list
# a. Membership
dict6 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
print('anak' in dict6)
print('wife' not in dict6)
