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
print('Remove using clear(), discard(), remove() and pop methods:')
# removes all the items from the dictionary by clear()
data1 = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}
data1.clear()
print(data1)
