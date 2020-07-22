# The zip() function is mainly used to combining data of two iterable elements together

idData = ['name', 'age', 'country', 'score']
attribute = ['saddam', 30, 'indonesia', 99]

for i, j in zip(idData, attribute):
    print(f'{i} : {j}')