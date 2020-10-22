print('1. String')
# a. String literals in python are surrounded by either single quotation marks, double or triple quotation marks.
print('Single Quotation Mark')
print("Double Quotation Mark")
print("""

Triple Quotation Mark
""") # multiline string

# b. Assign string to a variable and verify the data type using type() or isinstance() function
a = 'This is string'
print(a)
print(type(a))
print(isinstance(a, int))  # false because (a) is a string

print('\n2. Numeric')
# Integer
b = 123
print(b)
print(type(b))

# Float
c = 1.5
print(c)
print(type(c))

# Complex
d = 2 + 3j
print(d)
print(type(d))

print('\n3. Boolean')
# a. Booleans represent one of two values: True or False.
e = 2 > 1
f = 2 < 1
print(e)
print(f)
print(type(e))

print('\n4. List')
# List is a collection which is ordered and changeable. In Python lists are written with square brackets.
inilist = [1, 2.5, 'tiga', 4, True]
print(inilist)
print(type(inilist))

print('\n5. Tuple')
# Tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
inituple1 = (1, 2.5, 'tiga', 4, True)
inituple2 = 1, 2.5, 'tiga', 4, True  # a value without any brackets is also a tuple
print(inituple1)
print(type(inituple1))
print(inituple2)
print(type(inituple2))

print('\n6. Set')
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
iniset = {1, 2.5, 'tiga', 4, True}
print(iniset)
print(type(iniset))

print('\n7. Dictionary')
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
kamus_ind_eng = {
    'anak' : 'son',
    'istri' : 'wife',
    'ayah' : 'father',
    'ibu' : 'mother'
}
print(kamus_ind_eng)
print(type(kamus_ind_eng))

