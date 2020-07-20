# Dictionary as iterable

# Sample 1 (Key)
idFoods1 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for i in idFoods1:
    print(i)

print('-' * 100)

# Sample 2 (Value)
idFoods2 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for j in idFoods2:
    print(idFoods2[j])

print('-' * 100)

# Sample 3 (Key & Value)
idFoods3 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for k in idFoods3:
    print(f'{k} : {idFoods3[k]}')

print('-' * 100)

# Sample 4 (Combine with function)
idData1 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

key = []
value = []

for m in idData1:
    key.append(m) # Adds an element at the end of the empty list

for n in idData1.values():
    value.append(n)

for o, p in zip(key, value):  # zip() function is mainly used to combining data of two iterable elements together
    print(f'{o} : {p}')
