# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with
# curly brackets, and they have keys and values.


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

# 3. Change / assign items values
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
print()

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
# the parameter is in key not value
print('anak' in dict6)
print('wife' in dict6)
print()

# 7. Other samples in dictionaries
# a. Inline dictionaries
dict7 = {1: 'satu', 2: 'dua', 3: 'tiga'}
print(dict7)
print()

# b. Nested dictionaries
dict8 = {
    'satu': {
        101: 'saddam',
        102: 'rahmat',
        103: 'fuad',
        104: 'ali'
    },
    'dua': {
        105: 'along',
        106: 'wati',
        107: 'aini',
        108: 'yati',
        109: 'fitri',
        110: ['bonda', 'ratna']
    }
}
print(dict8)
print(dict8['satu'])
print(dict8['dua'][109])
print(dict8['dua'][110][1])
print()

# c. Memberlist dictionaries
dict9 = {
    'NIM': 110,
    'Nama': 'Saddam Husein',
    'Alamat': 'Keuangan Negara St.',
    'Kode Pos': 85111
}
dict10 = {
    'NIM': 111,
    'Nama': 'Rahmat Husein',
    'Alamat': 'Keuangan Negara St. No. 2',
    'Kode Pos': 85113
}
memberDict = {110: dict9, 111: dict10}
print(memberDict)
print(memberDict[111]['Kode Pos'])
print()

# d. Assign to empty dictionaries
dict11 = {}
dict11['anak'] = 'son'
dict11['istri'] = 'wife'
dict11['ayah'] = 'father'
dict11['ibu'] = 'mother'
print(dict11)

# e. Constructor dictionaries
dict12 = dict(satu= 1, dua= 2, tiga= 3, empat='empat')
print(dict12)
# integer as keys
dict13 = dict({1: "saddam", 2: "rahmat", 3: "fuad"})
print(dict13)

# f. Create dictionary by list as value
list1 = [1, 2, 3, 4]
dict12 = {}
dict12['satu'] = list1[0]
dict12['dua'] = list1[1]
dict12['tiga'] = list1[2]
dict12['empat'] = list1[3]
print(dict12)
